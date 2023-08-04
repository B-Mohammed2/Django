from django.db import models
#from datetime import datetime
# Create your models here.
class user_table(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    # date_of_birth=models.DateField(default=datetime.now)
    phone_number = models.CharField(max_length=15)