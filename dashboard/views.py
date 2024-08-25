from django.shortcuts import render, redirect
from work.models import ApplyJob, Work

# Create your views here.
def dashboard(request):
    return render(request , 'dashboard/dashboard.html')


        
