from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.nalu, name='nalu'),
    path('locations/', views.locations, name='locations'),
]