from django.db import models
from users.models import CustomUser
# Create your models here.

class Resume(models.Model):
    experience_choice = {
        ('Intern' , 'Intern'),
        ('Associate' , 'Associate'),
        ('Trainee' , 'Trainee'),
        ('Junior' , 'Junior'),
        ('Mid Level' , 'Mid Level'),
        ('Senior' , 'Senior'),

    }


    user = models.OneToOneField(CustomUser , on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True , blank=True)
    surname = models.CharField(max_length=100, null=True , blank=True)
    location = models.CharField(max_length=100, null=True , blank=True)
    job_title = models.CharField(max_length=100, null=True , blank=True)
    skills = models.TextField(null=True, blank=True)  
    experience_level = models.CharField(max_length=50, choices=experience_choice, null=True, blank=True)  
    upload_resume = models.FileField(upload_to='resume' , null=True , blank=True)

    def __str__(self):
        return f'{self.first_name} {self.surname}'
