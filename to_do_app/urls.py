from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_page, name='login'),
    path('index', views.index, name='index'),
    path('signup', views.signup_page, name='signup'),
    path('login', views.login_page, name='login'),
    path('update/<str:pk>/', views.update, name='update'),
    path('delete/<str:pk>/', views.delete, name='delete'),
    path('logout/', views.logout_page, name='logout'),
    path('logout-option/', views.logout_option, name='logout-option'),



]