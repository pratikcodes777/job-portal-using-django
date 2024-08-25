from django.db import models
from users.models import CustomUser
from company.models import Company
# Create your models here.

class Province(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Industry(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 


class Work(models.Model):
    job_type_choice = {
        ('Remote' , 'Remote'),
        ('Onsite' , 'Onsite'),
        ('Hybrid' , 'Hybrid'),
    }
    user = models.ForeignKey(CustomUser , on_delete=models.CASCADE)
    company = models.ForeignKey(Company , on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    salary = models.PositiveIntegerField()
    requirements = models.TextField()
    ideal_candidate = models.TextField()
    required_skills = models.TextField(null=True, blank=True) 
    is_available = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    industry = models.ForeignKey(Industry , on_delete=models.DO_NOTHING , null=True , blank=True)
    province = models.ForeignKey(Province , on_delete=models.DO_NOTHING , blank=True , null=True)
    job_type = models.CharField(max_length=50 , choices=job_type_choice , null=True , blank=True)

    def __str__(self):
        return self.title
    

class ApplyJob(models.Model):
    status_choices = [
        ('Accepted', 'Accepted'),
        ('Declined', 'Declined'),
        ('Pending', 'Pending'),
    ]
    user = models.ForeignKey(CustomUser , on_delete=models.CASCADE)
    job = models.ForeignKey(Work , on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20 , choices=status_choices)
