from django.urls import path
from patient import views

urlpatterns = [
    path("hello/",views.hello),
    path("echarts/",views.echarts,name='echarts'),
    path("pat/", views.pat),

]
