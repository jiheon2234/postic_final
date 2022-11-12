from django.shortcuts import render, get_object_or_404
from .models import *
from collections import defaultdict
from django.http import JsonResponse
from haversine import haversine
from .getcommon import getcommon
from django.db import connection
import pandas as pd


def showmain(request):  # 메인페이지
    return render(request, "showpage/showmain.html", None)


def showdetail(request, ann_no):  # 상세정보페이지
    ann = get_object_or_404(Announce, ann_no=ann_no)
    context = {"ann": ann}
    return render(request, "showpage/showdetail.html", context)


def regionjson(request):  # showstat json 주는 페이지

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


def showstat(request):  # 통계정보페이지
    # cur = connection.cursor()
    # worktype_list, paytype_list, pay_avg_list = [], [], []
    # sql = """select  count(*) as cnt,
    # round(avg(paymoney)/
    # case when paytype_no=3 then 174.4
    # when paytype_no=4 then 2092.8
    # else 1
    # end ,0) as avg
    # from announce
    # group by paytype_no
    # having paytype_no in (1,3,4)
    # order by paytype_no; """
    # cur.execute(sql)
    # for a, b in cur.fetchall():
    #     paytype_list.append(a)
    #     pay_avg_list.append(b)
    #     # pay_avg_list.append(int(b))
    # sql = """
    # select  count(*) as cnt from announce
    # group by worktype_no
    # order by worktype_no;
    # """
    # cur.execute(sql)
    # worktype_list = [x[0] for x in cur.fetchall()]

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


def showstat_occ(request):  # 직종별 통계정보 페이지
    # 데이터 프레임으로 바꾸기
    ann_df = pd.DataFrame.from_dict(
        Announce.objects.values(
            "ann_no", "company_no", "worktype_no", "paytype_no", "paymoney", "sido_no"
        )
    )
    com_df = pd.DataFrame.from_dict(Company.objects.values("com_no", "name", "sector"))
    pay_df = pd.DataFrame.from_dict(Paytype.objects.values("ptype_no", "type"))
    sido_df = pd.DataFrame.from_dict(Sido.objects.values("sido_no", "name", "momid"))
    work_df = pd.DataFrame.from_dict(Worktype.objects.values("wtype_no", "name"))

    # 모든 데이터 합치기
    df1 = pd.merge(ann_df, com_df, left_on="company_no", right_on="com_no")
    df1.rename(columns={"name": "company_name"}, inplace=True)
    df2 = pd.merge(df1, pay_df, left_on="paytype_no", right_on="ptype_no")
    df3 = pd.merge(df2, sido_df, how="left", on="sido_no")
    df3.rename(columns={"name": "sido_name"}, inplace=True)
    all_df = pd.merge(df3, work_df, left_on="worktype_no", right_on="wtype_no")
    all_df.rename(columns={"name": "work_name"}, inplace=True)
    # ------------------#
    # 직종별 채용건수
    work_by_job = all_df.groupby(["worktype_no"])["worktype_no"].count()
    work_by_job_txt = list(work_by_job)
    work_name = work_df["name"]  # work

    # 직종별 평균 월급 금액
    ptype_3 = all_df[all_df["paytype_no"] == 3]
    work_by_money = ptype_3.groupby(["worktype_no"])["paymoney"].mean()
    work_by_money_txt = list(round(work_by_money, 2))

    # 임금 현황
    paytype_list = [14875, 28892, 17502]  # 시급,월급,연봉

    # html로 값을 보내는 부분
    context = {
        "work_by_job_cnt": work_by_job_txt,
        "work_by_money_sum": work_by_money_txt,
        "paytype_list": paytype_list,
    }
    return render(request, "showpage/showstat_occ.html", context)


def showmap(request):  # 맞춤형 채용정보 페이지
    return render(request, "showpage/showmap.html", None)


def showmapjson(request):  # 맞춤형 채용정보 json주는페이지
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


def showkeyword(request):  # 키워드직접검색하는 페이지 (워드클라우드)
    return render(request, "showpage/showkeyword.html", None)


def showkeywordjson(request):  # 키워드직접검색, 선택으로 검색 json주는페이지
    kind = request.GET.get("kind", "sido")
    if kind == "sido":
        momid = request.GET.get("momid", 25)
        ann = Announce.objects.filter(sido_no__momid=momid)
    elif kind == "occ":
        occ = request.GET.get("occ", 1)
        print(occ)
        ann = Announce.objects.filter(title__contains=occ)
        print(ann[0].title)
    else:  # both
        momid = request.GET.get("momid", 25)
        occ = int(request.GET.get("occ_num", 1))
        occ_list = [x + 1 for x in range(13) if occ & 1 << x]
        print(occ_list)
        ann = Announce.objects.filter(sido_no__momid=momid, worktype_no__in=occ_list)
        print(ann.query)
    tmp = getcommon(ann, n=100)
    data = [{"x": t[0], "value": t[1]} for t in tmp]
    # print(data)
    return JsonResponse({"data": data})


def showkeyword_occ(request):  # 선택으로 키워드검색하는 페이지(워드클라우드)
    return render(request, "showpage/showkeyword_occ.html", None)
