from django.urls import path
from employee import views

app_name = 'emp'

urlpatterns = [
    path('', views.employee, name='employee'),
    path('branch', views.branch, name='branch'),
    path('registration', views.registration, name='registration'),
    path('login', views.user_login, name='user_login'),

]
