from django.db import models

# Create your models here.
class user_table(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    # date_of_birth = models.DateField(default='1970-01-01')
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(default='example@example.com')
    
class donation_table(models.Model):
    payment_ID=models.IntegerField()
    donation_amount= models.DecimalField(max_digits=10, decimal_places=2, null=True)
    donor_detaills=models.CharField(max_length=100, null=True)
    # date_and_time_of_donation=models.DateField()
    organizations_name=models.CharField()

class charities_organizations_name(models.Model):
    charities_organizations_name= models.CharField(max_length=50, primary_key=True)
    