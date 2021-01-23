from django.urls import path

from . import views

urlpatterns = [
    path('<int:question_id>/index/', views.index, name='index'),
    path('<int:question_id>/', views.nalu, name='nalu'),
    path('<int:question_id>/results/', views.results, name='results'),
]