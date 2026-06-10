from django.urls import path
from core import views

urlpatterns =[
    path('',views.home,name='home'),
    path('Login',views.login,name='login'),
    path('Submit/Login',views.submit_login,name='submit_login'),
    path('Logout',views.logout,name='logout'),
    
]