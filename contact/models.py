from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):                             
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"     
    
    def __str__(self) -> str:
        return self.name
    

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=250, blank=True)
    Created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    show = models.BooleanField(default=True)
    picture = models.ImageField(upload_to="pictures/%Y/%m/%d", blank=True)
    category = models.ForeignKey(Category, on_delete = models.SET_NULL, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} " 
