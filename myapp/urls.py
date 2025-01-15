
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
     path('login/', views.login, name='login'),
    path('welcome/', views.welcome_view, name='welcome'),
    path('logout/', views.logout, name='logout'),
     path('users/', views.user_list, name='user_list'),
     path('messages/', views.messages_view, name='messages'),
     path('messages/', views.messages_view, name='message'),  # typo in name here
path('messages/', views.messages_view, name='messages'),
  path('internal_marks/', views.internal_marks, name='internal_marks'),
  path('update_marks/<int:id>/', views.update_marks, name='update_marks'),
    path('upload_marks/', views.upload_marks, name='upload_marks'),
]
