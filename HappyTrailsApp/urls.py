from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.nalu, name='nalu'),
    path('locations/', views.locations, name='locations'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)