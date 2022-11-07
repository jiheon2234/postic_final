from django.urls import path
from .views import *

app_name = "showpage"
urlpatterns = [
    path("", showmain, name="main"),  # 메인
    path("showstat_occ", showstat_occ, name="showstat_occ"),  # 직종별 통계
    path("showstat", showstat, name="showstat"),  # 지역별 통계
    path("regionjson", regionjson),  # json
    path("showmap", showmap, name="showmap"),  # 맞춤형
    path("showmapjson", showmapjson),  # 맞춤형 페이지 json
    path("showdetail/<int:ann_no>", showdetail),  # 공고 상세 페이지
    path("showkeyword", showkeyword, name="showkeyword"),  # 검색형 워드클라우드
    path("showkeywordjson", showkeywordjson),  # 워드클라우드 json
    path("showkeyword_occ", showkeyword_occ, name="showkeyword_occ"),  # 선택형 워드클라우드
]
