from django.urls import path

from sym import views

urlpatterns = [
    path("hello/",views.hello),
    path('symall/',views.show)
]
