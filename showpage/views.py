from django.shortcuts import render, get_object_or_404
from .models import *
from collections import defaultdict
from django.http import JsonResponse
from haversine import haversine


def showdetail(request, ann_no):
    ann = get_object_or_404(Announce, ann_no=ann_no)
    context = {"ann": ann}
    return render(request, "showpage/showdetail.html", context)


def regionjson(request):
    region = int(request.GET.get("region", 11))
    ann = (
        Announce.objects.filter(sido_no__momid=region)
        if region < 100
        else Announce.objects.filter(sido_no=region)
    )
    worktype_list = [len(ann.filter(worktype_no=i)) for i in range(1, 14)]
    tmp = [ann.filter(paytype_no=i) for i in (1, 3, 4)]
    paytype_list = [len(x) for x in tmp]
    pay_avg_list = [sum([*map(lambda x: x.paymoney, t)]) for t in tmp]
    pay_avg_list[0], pay_avg_list[1], pay_avg_list[2] = (
        int(pay_avg_list[0] / paytype_list[0]),
        int(pay_avg_list[1] / paytype_list[1] / 174.4),
        int(pay_avg_list[2] / paytype_list[2] / 2092.8),
    )
    res = {
        "worktype_list": worktype_list,
        "paytype_list": paytype_list,
        "pay_avg_list": pay_avg_list,
    }
    # print(res)
    return JsonResponse(res)


# Create your views here.
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


def showstat_occ(request):
    return render(request, "showpage/showstat.html", None)


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
