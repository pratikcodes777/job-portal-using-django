from django.db import models
from users.models import CustomUser
# Create your models here.

class Company(models.Model):
    user = models.OneToOneField(CustomUser , on_delete=models.CASCADE)
    name = models.CharField(max_length=100 , null=True , blank=True)
    est_date = models.PositiveIntegerField(null=True , blank=True)
    city = models.CharField(max_length=100, null=True , blank=True)
    province = models.CharField(max_length=100, null=True , blank=True)

    def __str__(self):
        return self.name
