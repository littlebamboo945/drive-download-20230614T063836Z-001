from django.urls import path, include
from api import views

urlpatterns = [
    path('', views.form),
    path('chat/', views.chat),
]
