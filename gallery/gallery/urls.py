from django.urls import path
from igalleryapp import views


urlpatterns = [
    path('', views.index, name='index'),
]

