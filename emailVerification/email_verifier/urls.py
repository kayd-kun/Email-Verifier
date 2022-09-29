from django.urls import URLPattern, path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
]