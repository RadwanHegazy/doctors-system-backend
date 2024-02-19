from django.urls import path
from .views import login, get

urlpatterns = [
    path('login/',login.LoginView),
    path('get/departments/',get.GetAllDepartments),
    path('profile/',get.DoctorProfile),
]