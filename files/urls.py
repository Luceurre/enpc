from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sections', views.sections, name='sections'),
    path('sections/<str:section>', views.files, name='files')
]