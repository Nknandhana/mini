
from django.urls import path
from . import views

urlpatterns = [
   path('signup/', views.signup, name='signup'),
     path('login/', views.login, name='login'),
    path('welcome/', views.welcome_view, name='welcome'),
    path('logout/', views.logout, name='logout'),
     path('users/', views.user_list, name='user_list'),
     

  path('internal_marks/', views.internal_marks, name='internal_marks'),
   path('upload/', views.index, name='upload'),
     path('profile/', views.profile, name='profile'),

     path('register/<int:subject_id>/', views.register_subject, name='register_subject'),
    path('view_marks/<int:subject_id>/', views.view_marks, name='view_marks'),

    

    
     path('faculty_home/', views.faculty_home, name='faculty_home'),
    path('student_home/', views.student_home, name='student_home'),
      path('add_course/', views.add_course, name='add_course'),
      path('faculty_login/', views.faculty_login, name='faculty_login'),
    path('internal_marks/', views.internal_marks, name='internal_marks'),
]
   
  
