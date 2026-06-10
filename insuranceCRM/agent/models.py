from django.db import models
from crm_admin.models import AgentModel,CampaginModel

# Create your models here.

class ClientModel(models.Model):

    agent = models.ForeignKey(AgentModel,on_delete=models.SET_NULL,null=True)
    campagin = models.ForeignKey(CampaginModel,on_delete=models.SET_NULL,null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    married_status = models.CharField(max_length=20)
    aadhaar_number = models.CharField(max_length=12)
    pan_number = models.CharField(max_length=10)
    job = models.TextField(null=True)
    qulification = models.TextField(null=True)
    previous_policy = models.CharField(max_length=5,null=True)
    previous_policy_number = models.CharField(max_length=50,null=True,blank=True)
    same_policy = models.CharField(max_length=5,null=True)
    agent_feedback = models.TextField(null=True,blank=True)
    campaign_feedback = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to="client/",null=True)