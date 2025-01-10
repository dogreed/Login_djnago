

from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('login/' , views.loginpage, name='login'),
    path('signup/', views.signup, name='signup'),
    path('login/signup/', views.signup, name='signup'),
    path('news', views.news, name="news"),
    path('image', views.image, name="image"),  

]
