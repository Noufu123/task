from app1 import views
from django.urls import path

urlpatterns=[
    path('',views.home,name="home"),
    path('sign_up',views.sign_up,name="sign_up"),
    path('login',views.login,name="login"),

    path('signup_page',views.signup_page,name="signup_page"),
    path('login_page',views.login_page,name="login_page"),
    path('logout',views.logout,name="logout"),
]