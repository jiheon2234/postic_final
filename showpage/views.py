from django.shortcuts import render, get_object_or_404
from .models import *
from collections import defaultdict
from django.http import JsonResponse
from haversine import haversine
from .getcommon import getcommon

#############$####### 메인


def showmain(request):
    return render(request, "showpage/showmain.html", None)


#############$####### 메인끝


#######################상세페이지
def showdetail(request, ann_no):
    ann = get_object_or_404(Announce, ann_no=ann_no)
    context = {"ann": ann}
    return render(request, "showpage/showdetail.html", context)


#######################상세페이지 끝


##########################지역별 통계정보
def regionjson(request):

    region = int(request.GET.get("region", 11))
    if region < 1000:
        ann = Announce.objects.filter(sido_no__momid=region)
        child_sido = [
            *map(
                lambda x: {"sido_no": x.sido_no, "name": x.name}, Sido.objects.filter(momid=region)
            )
        ]

    else:
        child_sido = None
        ann = Announce.objects.filter(sido_no=region)

    worktype_list = [len(ann.filter(worktype_no=i)) for i in range(1, 14)]
    tmp = [ann.filter(paytype_no=i) for i in (1, 3, 4)]
    paytype_list = [len(x) for x in tmp]
    ##시발##
    pay_avg_list = [sum([*map(lambda x: x.paymoney, t)]) for t in tmp]
    pay_avg_list[0] = (
        int(pay_avg_list[0] / paytype_list[0]) if pay_avg_list[0] or paytype_list[0] else 0
    )
    pay_avg_list[1] = (
        int(pay_avg_list[1] / paytype_list[1] / 174.4) if pay_avg_list[1] and paytype_list[1] else 0
    )
    pay_avg_list[2] = (
        int(pay_avg_list[2] / paytype_list[2] / 2092.8)
        if pay_avg_list[2] and paytype_list[2]
        else 0
    )
    print(pay_avg_list)

    res = {
        "worktype_list": worktype_list,
        "paytype_list": paytype_list,
        "pay_avg_list": pay_avg_list,
        "child_sido": child_sido,
    }
    # print(res)

    return JsonResponse(res)


def showstat(request):
    ann = Announce.objects.all()
    worktype_list = [10339, 3679, 2385, 6617, 890, 11418, 6084, 1739, 6831, 2965, 2619, 5872, 344]
    paytype_list = [14875, 28892, 17502]  # 시급,월급,연봉
    pay_avg_list = [10647, 13071, 15060]  # 시급, 월급, 연봉을 시급으로
    context = {
        "worktype_list": worktype_list,
        "paytype_list": paytype_list,
        "pay_avg_list": pay_avg_list,
    }
    return render(request, "showpage/showstat.html", context)


##########################지역별 통계정보 끝


#########################직종별 통계정보
def showstat_occ(request):
    return render(request, "showpage/showstat.html", None)


#########################직종별 통계정보 끝


#######################맞춤형채용정보
def showmap(request):
    return render(request, "showpage/showmap.html", None)


def showmapjson(request):
    n, xx, yy = (
        int(request.GET.get("n", 5)),
        float(request.GET.get("cx", 127.4267524)),
        float(request.GET.get("cy", 36.350107)),
    )
    # print(xx, yy)
    if xx == 0 or yy == 0:
        xx, yy = (36.350107, 127.4267524)
    print(xx, yy)
    start = (xx, yy)
    anns_list = [
        *map(
            lambda x: {
                "title": x.title,
                "ann_no": x.ann_no,
                "address": x.sido_no.name,
                "distance": int(haversine(start, (float(x.y), float(x.x)), unit="m")),
                "x": x.x,
                "y": x.y,
            },
            (
                sorted(
                    list(Announce.objects.filter(x__isnull=False)),
                    key=lambda obj: haversine(start, (float(obj.y), float(obj.x))),
                )[:n]
            ),
        )
    ]
    res = {"anns_list": anns_list}
    # print(res)
    return JsonResponse(res)


#######################맞춤형채용정보 끝


##############################지역별 워드클라우드
def showkeyword(request):
    return render(request, "showpage/showkeyword.html", None)


def showkeywordjson(request):
    kind = request.GET.get("kind", "sido")
    if kind == "sido":
        momid = request.GET.get("momid", 25)
        ann = Announce.objects.filter(sido_no__momid=momid)
    elif kind == "occ":
        occ = request.GET.get("occ", 1)
        ann = Announce.objects.filter(worktype_no=occ)
    else:
        momid = request.GET.get("momid", 25)
        occ = request.GET.get("occ", 1)
        ann1 = Announce.objects.filter(sido_no__momid=momid)
        ann2 = Announce.objects.filter(worktype_no=occ)
        ann = ann1 | ann2
    tmp = getcommon(ann, n=100)
    data = [{"x": t[0], "value": t[1]} for t in tmp]
    # print(data)
    return JsonResponse({"data": data})


def showkeywordoccjson(request):
    pass


##############################지역별 워드클라우드 끝


############################## 직종별 워드클라우드


def showkeyword_occ(request):
    return render(request, "showpage/showkeyword_occ.html", None)


############################## 직종별 워드클라우드 끝
