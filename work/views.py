from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import CreateJobForm, UpdateJobForm
from users.models import CustomUser
from work.models import Work, ApplyJob
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from resume.models import Resume
from .utils import calculate_match_score


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
    messages.info(request , 'Job applied successfully.')
    return redirect('applied-jobs')


def cancel_applied_job(request, pk):
    applied_job = ApplyJob.objects.get(pk=pk, user=request.user)
    
    if applied_job.status == 'Pending':
        applied_job.delete()
        messages.success(request, 'Your job application has been canceled.')
    else:
        messages.warning(request, 'You can only cancel applications with a "Pending" status.')

    return redirect('applied-jobs')

# def all_applicants(request, pk):
#     job = Work.objects.get(pk=pk)
#     applicants = job.applyjob_set.all()
#     context = {
#         'job': job,
#         'applicants': applicants
#     }
#     return render(request , 'work/all_applicants.html' , context)

def all_applicants(request, pk):
    job = Work.objects.get(pk=pk)
    applicants = job.applyjob_set.all()

    if request.method == 'POST':
        applicant_id = request.POST.get('applicant_id')
        action = request.POST.get('action')  
        
        applicant = ApplyJob.objects.get(pk=applicant_id)
        if action == 'accept':
            applicant.status = 'Accepted'
            applicant.save()

            # message 
            subject = f'Job Application Accepted for {job.title}'
            message = f'You have been selected for the {job.title} position at {job.company.name}.'
            plain_message = strip_tags(message)
            from_email = settings.DEFAULT_FROM_EMAIL
            to = applicant.user.email

            # Send email
            send_mail(subject, plain_message, from_email, [to])

            messages.success(request, f'{applicant.user.email} has been notified about the acceptance.')
        elif action == 'reject':
            applicant.status = 'Rejected'
            applicant.save()
            messages.info(request, f'{applicant.user.email} application rejected.')

    context = {
        'job': job,
        'applicants': applicants
    }
    return render(request, 'work/all_applicants.html', context)


def applied_jobs(request):
    jobs = ApplyJob.objects.filter(user = request.user)
    context = {
        'jobs': jobs
    }
    return render(request , 'work/applied_jobs.html' , context)


def recommend_jobs(request):
    user = request.user
    resume = Resume.objects.get(user=user) 
    applicant_skills = resume.skills if resume.skills else ""
    
    jobs = Work.objects.filter(is_available=True)  
    job_recommendations = []

    for job in jobs:
        job_required_skills = job.required_skills if job.required_skills else ""
        score = calculate_match_score(applicant_skills, job_required_skills)
        job_recommendations.append((job, score))
    

    job_recommendations = sorted(job_recommendations, key=lambda x: x[1], reverse=True)
    context ={
        'job_recommendations': job_recommendations
    }
    
    return render(request, 'work/recommendations.html',context )

