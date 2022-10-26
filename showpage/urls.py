from django.urls import path
from . import views

app_name = "showpage"
urlpatterns = [
    path("", views.showstat),
    path("showstat_occ", views.showstat_occ, name="showstat_occ"),
    # path("showstat", views.showstat,name='showstat),
    path("regionjson", views.regionjson),
    path("showmap", views.showmap, name="showmap"),
    path("showmapjson", views.showmapjson),
    path("showdetail/<int:ann_no>", views.showdetail),
]
