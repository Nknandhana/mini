from django.db import models

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