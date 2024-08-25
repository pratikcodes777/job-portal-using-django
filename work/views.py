from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CreateJobForm, UpdateJobForm
from users.models import CustomUser
from work.models import Work, ApplyJob


def create_job(request):
    if request.method == 'POST':
        form = CreateJobForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.user = request.user
            var.company = request.user.company
            var.save()
            messages.success(request , 'Job Created Successfully.')
            return redirect('dashboard')
        else:
            messages.warning(request , 'Something went wrong.')
            return redirect('dashboard')
    else:
        form = CreateJobForm()
        context = {
            'form': form
        }
        return render(request , 'work/create_job.html' , context)



def update_job(request, pk):
    job_to_update = Work.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateJobForm(request.POST , instance=job_to_update)
        if form.is_valid():
            form.save()
            messages.success(request , 'Job Info updated Successfully.')
            return redirect('manage-jobs')
        else:
            messages.warning(request , 'Something went wrong.')
            return redirect('dashboard')
    else:
        form = UpdateJobForm(instance=job_to_update)
        context = {
            'form': form
        }
        return render(request , 'work/update_job.html' , context)
    

def manage_jobs(request):
    jobs = Work.objects.filter(user = request.user , company = request.user.company)
    context = {
        'jobs': jobs
    }
    return render(request, 'work/manage_jobs.html' , context) 


def apply_to_jobs(request, pk):
    job_to_apply = Work.objects.get(pk=pk)
    ApplyJob.objects.create(
        job = job_to_apply,
        user = request.user,
        status = 'Pending'
    )
    messages.info(request , 'Job applied successfully. Please see the dashboard.')
    return redirect('dashboard')


def all_applicants(request, pk):
    job = Work.objects.get(pk=pk)
    applicants = job.applyjob_set.all()
    context = {
        'job': job,
        'applicants': applicants
    }
    return render(request , 'work/all_applicants.html' , context)


def applied_jobs(request):
    jobs = ApplyJob.objects.filter(user = request.user)
    context = {
        'jobs': jobs
    }
    return render(request , 'work/applied_jobs.html' , context)

