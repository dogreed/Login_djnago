

from . import views
from django.urls import path


urlpatterns = [
    
    path('', views.home, name='home'),
    # path('home', views.home, name='home'),
    path('news/', views.news, name="news"),

    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutv, name='logout'),
  
      

    # for admin page
    path('adminmain/', views.admin, name='admin'),
    path('addnews/', views.addnews, name='addnews'),

    #for delete news 
    path('delete/<int:news_id>/', views.delete_news, name='delete_news'),  
]

