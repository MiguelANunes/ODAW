from django.urls import path
from mainApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:num>/', views.detail, name='detail'),
    path('login/', views.login, name='login')
]