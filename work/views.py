from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CreateJobForm, UpdateJobForm
from users.models import CustomUser
from work.models import Work


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
            return redirect('dashboard')
        else:
            messages.warning(request , 'Something went wrong.')
            return redirect('dashboard')
    else:
        form = UpdateJobForm(instance=job_to_update)
        context = {
            'form': form
        }
        return render(request , 'work/update_job.html' , context)