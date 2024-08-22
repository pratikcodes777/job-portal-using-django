from django.shortcuts import render
from work.models import Work, ApplyJob

# Create your views here.
def home(request):
    return render(request , 'index.html')


def job_listing(request):
    jobs = Work.objects.filter(is_available = True).order_by('-timestamp')
    context = {
        'jobs': jobs
    }
    return render(request , 'website/job_listing.html' , context)


def job_details(request , id):
    job_applied = ApplyJob.objects.filter(user = request.user , job=id)
    if job_applied.exists():
        is_applied = True
    else:
        is_applied= False
    job = Work.objects.get(id=id)
    context = {
        'job': job,
        'is_applied':is_applied
    }
    return render(request, 'work/job_details.html', context)