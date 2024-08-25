from django.shortcuts import render, get_object_or_404
from work.models import Work, ApplyJob
from .filter import JobFilter

# Create your views here.
def home(request):
    filter = JobFilter(request.GET , queryset = Work.objects.filter(is_available = True).order_by('-timestamp'))
    context = {
        'filter':filter
    }
    return render(request , 'index.html' , context)


def job_listing(request):
    jobs = Work.objects.filter(is_available = True).order_by('-timestamp')

    context = {
        'jobs': jobs,

    }
    return render(request , 'website/job_listing.html' , context)


# def job_details(request , id):
#     job_applied = ApplyJob.objects.filter(user = request.user , job=id)
#     if job_applied.exists():
#         is_applied = True
#     else:
#         is_applied= False
#     job = Work.objects.get(id=id)
#     context = {
#         'job': job,
#         'is_applied':is_applied
#     }
#     return render(request, 'work/job_details.html', context)


def job_details(request, id):
    job = Work.objects.get(id=id)
    job_applied = ApplyJob.objects.filter(user=request.user, job=job).first()
    is_applied = job_applied is not None
    applied_job_pk = job_applied.pk if job_applied else None

    context = {
        'job': job,
        'is_applied': is_applied,
        'applied_job_pk': applied_job_pk
    }
    return render(request, 'work/job_details.html', context)