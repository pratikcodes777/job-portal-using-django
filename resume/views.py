from django.shortcuts import render, redirect
from .models import Resume
from users.models import CustomUser
from django.contrib import messages
from .forms import UpdateResume


def update_resume(request):
    if request.user.is_applicant:
        resume = Resume.objects.get(user = request.user)
        if request.method == 'POST':
            form = UpdateResume(request.POST , instance=resume)
            if form.is_valid:
                var  = form.save(commit=False)
                user = CustomUser.objects.get(id = request.user.id)
                user.has_resume = True
                var.save()
                user.save()
                messages.success(request , 'Resume updated successfully.')
                return redirect('dashboard')
            else:
                messages.warning(request , 'Something went wrong.')
                return redirect('dashboard')
        else:
            form = UpdateResume(instance=resume)
            context = {
                'form': form
            }
        return render(request ,'resume/update_resume.html', context)
    else:
        messages.warning(request , 'Permisssion denied')
        return redirect('dashboard')
    

def resume_details(request , pk):
    resume = Resume.objects.get(id=pk)
    context = {
        'resume': resume
    }
    return render(request , 'resume/resume_details.html' , context)
