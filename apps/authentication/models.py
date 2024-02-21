from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    farmer = 'farmer'
    agrics_officer = 'agrics_officer'
    ADMIN = 'admin'
  
    ROLE_CHOICES = [
        (farmer, 'farmer'),
        (agrics_officer, 'agrics_officer'),
        (ADMIN, 'Admin'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=farmer)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # Add more fields as needed

class AnthraxSymptom(models.Model):
    farmer = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="farmer")
    # agrics_officer = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='agrics_officer')
    farmer_name = models.CharField(max_length=255,null=True, blank=True)
    animal_name = models.CharField(max_length=255,null=True, blank=True)
    animal_age = models.IntegerField(null=True, blank=True)  # You can change the data type as needed
    location = models.CharField(max_length=255,null=True, blank=True)
    phone_number = models.CharField(max_length=15,null=True, blank=True)  # You can adjust the maximum length based on your needs
    symptoms = models.CharField(max_length=1000,null=True, blank=True)
    recommendation = models.CharField(max_length=10000,null=True, blank=True)
    def __str__(self):
	        return f'{self.first_name}   {self.last_name} {self.username} '