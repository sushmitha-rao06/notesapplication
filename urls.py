
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.dashboard),
    path('signup',views.render_signup_page),
    path('login',views.render_login_page),
    path('signup_user', views.signup_user),
    path('login_user', views.login_user),
    path('dashboard/', views.dashboard),
    path('savenotes', views.savenotes),
    path('delete_note', views.delete_notes),
    
]
