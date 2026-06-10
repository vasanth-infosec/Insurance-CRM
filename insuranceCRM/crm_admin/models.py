from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()

# Create your models here.

class AgentModel(models.Model):
     admin = models.ForeignKey(user,on_delete=models.SET_NULL,null=True)
     pnumber = models.CharField(max_length=15)
     specialization = models.TextField()
     image = models.ImageField(upload_to="agent/")

class CampaginModel(models.Model):
     agent = models.ForeignKey(AgentModel,on_delete=models.SET_NULL,null=True)
     name = models.TextField()
     date = models.DateField()
     time = models.TimeField()
     location = models.CharField(max_length=100)