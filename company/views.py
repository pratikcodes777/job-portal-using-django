from django.shortcuts import render, redirect
from users.models import CustomUser 
from .models import Company
from users.models import CustomUser
from django.contrib import messages
from .forms import UpdateCompamy


# update company 
def update_company(request):
    if request.user.is_recruiter:
        company = Company.objects.get(user = request.user)
        if request.method == 'POST':
            form = UpdateCompamy(request.POST , instance= company)
            if form.is_valid():
                var = form.save(commit = False)
                user = CustomUser.objects.get(id = request.user.id)
                user.has_company = True
                var.save()
                user.save()
                messages.info(request , 'Your company info has been updated.')
                return redirect('dashboard')
            else:
                messages.warning(request , 'Something went wrong.')
            
        else:
            form = UpdateCompamy(instance = company)
            context = {
                'form': form
            }
        return render(request , 'company/update_company.html' , context)
    else:
        messages.warning(request , 'Permission Denied')
        return redirect('dashboard')


# view company detail
def company_details(request , pk):
    company = Company.objects.get(pk=pk)
    context = {
        'company': company
    } 
    return render(request , 'company/company_details.html' , context)


# create jobs 
def create_jobs(request):
    pass

