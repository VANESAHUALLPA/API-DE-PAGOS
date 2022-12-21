from django.db import models
from users.models import User

class Services(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=45)
    logo = models.URLField(max_length=45)
    
class Payment_user(models.Model):
    id = models.AutoField(primary_key=True)
    User_id = models.ForeignKey(User, on_delete =models.CASCADE, related_name='Services')
    Service_id = models.CharField(Foringkey_length=45)
    Amount = models.IntegerField(max_length=5)
    PaymentDate = models.DateField(auto_now_add=True)
    ExpirationDate = models.DateField(auto_now_add=True)

class Expired_payments(models.Model):
    id = models.AutoField(primary_key=True)
    Payment_user_id = models.CharField(max_length=80)
    Penalty_fee_amount = models.CharField(max_length=45)
 
class User(models.Model)   
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=80, unique=True, default="no@email.com")
    username = models.CharField(max_length=45)
    Password = models.CharField(max_length=45)
