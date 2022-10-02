from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class usermodel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    user_Photo=models.ImageField(null=True,blank=True,upload_to='image/')
    user_address=models.CharField(max_length=250)
    user_number=models.IntegerField()