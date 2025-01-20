from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class User(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)

    def __str__(self):
        return self.username
class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Student(models.Model):
    name = models.CharField(max_length=100)
    register_number = models.CharField(max_length=20, unique=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam_1 = models.IntegerField(default=0)
    exam_2 = models.IntegerField(default=0)
    exam_3 = models.IntegerField(default=0)
    exam_4 = models.IntegerField(default=0)

    def average_marks(self):
        return (self.exam_1 + self.exam_2 + self.exam_3 + self.exam_4) / 4

    def total_marks(self):
        return self.exam_1 + self.exam_2 + self.exam_3 + self.exam_4

    def __str__(self):
        return f"Marks for {self.student.name}"
    

    
    
class Note(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='notes/')
    faculty = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    


class Course(models.Model):
    course_name = models.CharField(max_length=200)

    def __str__(self):
        return self.course_name
    

class Class(models.Model):
    class_name = models.CharField(max_length=100)
# You can add more fields like description, etc.

    def __str__(self):
        return self.class_name
    




    
    
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    user_class = models.ForeignKey(Class, null=True, blank=True, on_delete=models.SET_NULL)
    TYPE_CHOICES = [
        ('student', 'Student'),
        ('faculty', 'Faculty'),
    ]
    user_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='student')

    def clean(self):
        if self.user_type == 'faculty' and self.user_class:
            raise ValidationError('Faculty members cannot have a class assigned.')

    def __str__(self):
        return f"{self.user.username} "
    
class Course(models.Model):
    course_name= models.CharField(max_length=255, null=True, blank=True)
    class_obj=models.ForeignKey(Class, null=True, blank=True, on_delete=models.SET_NULL)
    teacher=models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    def __str__(self):
        return f"{self.course_name} "
    

class Attendence(models.Model):
    student=models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    course=models.ForeignKey(Course, null=True, blank=True, on_delete=models.SET_NULL)
    present=models.IntegerField()
    date=models.DateField()
    period=models.IntegerField()
    max_mark=models.IntegerField(null=True,blank=True)
    def __str__(self):
        return f"{self.student.name} "
    


    
