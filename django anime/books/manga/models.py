from django.db import models

# Create your models here.
class Login(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    re_password=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
 
class Category(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name

class Mangafiles(models.Model):
    pdf=models.FileField()
    name=models.CharField(max_length=100)
    def __str__(self):
        return str(self.pdf)
    
class Anime(models.Model):
    image=models.ImageField()
    name=models.CharField(max_length=50)
    bio=models.TextField()
    manga=models.FileField()
    link=models.URLField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    files=models.ManyToManyField(Mangafiles)
    def __str__(self):
        return self.name