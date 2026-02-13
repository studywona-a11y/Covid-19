from django.urls import path

from home import views
from patient import views as pa_views
from sym import views as sym_views
urlpatterns = [
    path("hello/",views.home),
    path("",views.index,name='index'),
    path("first/map", views.map, name='map'),
    path("first/movie", views.movie, name='movie'),
    path("first/pie", views.pie, name='pie'),
    path("first/rank", views.rank, name='rank'),
    path("first/patient", pa_views.pat, name='patient'),
    path("first/sym",sym_views.show, name='sym'),
]
