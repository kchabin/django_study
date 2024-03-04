from django.urls import path
from . import views

urlpatterns = [
    #url과 그 url이 들어올 때 어떻게 처리할 지 명시한다.
    path('', views.index),
]