from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    gun = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    username = models.ForeignKey(User, to_field='username', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name