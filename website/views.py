from django.shortcuts import render
from work.models import Work

# Create your views here.
def home(request):
    return render(request , 'index.html')


def job_listing(request):
    jobs = Work.objects.filter(is_available = True)
    context = {
        'jobs': jobs
    }
    return render(request , 'website/job_listing.html' , context)


def job_details(request , id):
    job = Work.objects.get(id=id)
    context = {
        'job': job
    }
    return render(request, 'work/job_details.html', context)