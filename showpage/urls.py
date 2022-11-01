from django.urls import path
from .views import *

app_name = "showpage"
urlpatterns = [
    path("", showstat),
    path("showstat_occ", showstat_occ, name="showstat_occ"),
    path("showstat", showstat, name="showstat"),
    path("regionjson", regionjson),
    path("showmap", showmap, name="showmap"),
    path("showmapjson", showmapjson),
    path("showdetail/<int:ann_no>", showdetail),
    path("showkeyword", showkeyword, name="showkeyword"),
    path("showkeywordjson", showkeywordjson),  # 지역별 json
    path("showkeywordoccjson", showkeywordoccjson),  # 직종별 json
    path("showkeyword_occ", showkeyword_occ, name="showkeyword_occ"),
]
