from django.urls import path

from webprojectapp import views

urlpatterns = [
    path('', views.fun1, name='fun'),
    path('register', views.register, name='register'),
    path('login_section', views.loginpage, name='login'),
    path('logout', views.logout, name='logout')
]
