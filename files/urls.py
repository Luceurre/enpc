from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/sections', views.api_sections, name='api.sections'),
    path('api/sections/<str:section>', views.api_files, name='api.files'),
    path('sections', views.sections, name='sections'),
    path('sections/<str:section>', views.files, name='files')
]