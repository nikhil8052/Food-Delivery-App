from django.db import models
from base.models import BaseModel
from django.contrib.auth.models import User

class Order(BaseModel):
    payment_status=models.CharField(max_length=100, null=True, blank=True)
    order_id=models.CharField(max_length=100, null=True,blank=True)
    payment_id=models.CharField(max_length=100, null=True,blank=True)
    payment_signature=models.CharField(max_length=100, null=True,blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='user')
    amount=models.IntegerField(null=True) 
    