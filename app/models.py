from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#smaraki models is ur job and forms too
class Profile(models.Model):
    username=models.ForeignKey(User, on_delete=models.CASCADE)
    pno=models.CharField(max_length=100)

    def __str__(self):
        return self.username.username
    
class Todo(models.Model):
    username=models.ForeignKey(User, on_delete=models.CASCADE)
    Sl_No=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=100)
    desc=models.CharField(max_length=250)

    def __str__(self):
        return self.title[:12]