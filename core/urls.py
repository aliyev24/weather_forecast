from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('registration/', views.RegisterUser.as_view(), name='registration'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_me, name='logout'),
    path('user/', views.user, name='user'),
    ]