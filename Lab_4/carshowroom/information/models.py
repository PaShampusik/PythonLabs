from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    image = models.ImageField(upload_to='articles/')
    content = models.TextField()

    def get_absolute_url(self):
        return reverse('information:news', args=[])
    

class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

class Employee(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='employees/')
    description = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    rating = models.IntegerField()
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Promotion(models.Model):
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.code