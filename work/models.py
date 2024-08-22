from django.db import models
from users.models import CustomUser
from company.models import Company
# Create your models here.

class Work(models.Model):
    user = models.ForeignKey(CustomUser , on_delete=models.CASCADE)
    company = models.ForeignKey(Company , on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    salary = models.PositiveIntegerField()
    requirements = models.TextField()
    ideal_candidate = models.TextField()
    is_available = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class ApplyJob(models.Model):
    status_choices = {
        ('Accepted' , 'Accepted'),
        ('Declined' , 'Declined'),
        ('Pending' , 'Pending')
    }
    user = models.ForeignKey(CustomUser , on_delete=models.CASCADE)
    job = models.ForeignKey(Work , on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20 , choices=status_choices)
