from django.urls import path
from app_web import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
]
