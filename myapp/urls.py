
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
     path('login/', views.login, name='login'),
    path('welcome/', views.welcome_view, name='welcome'),
    path('logout/', views.logout, name='logout'),
     path('users/', views.user_list, name='user_list'),
]
