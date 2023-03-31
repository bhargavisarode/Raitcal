from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.login, name='logintype'),
    path('loginpage/', views.logintype, name='loginpage'),
    path('register/', views.register, name='register'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('index/', views.index, name='index'),

]