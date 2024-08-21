from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from .models import CustomUser
from .forms import RegisterForm
from resume.models import Resume
from company.models import Company
# Create your views here.

User = get_user_model()




# registration of applicant 
def register_applicant(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            val = form.save(commit=False)
            val.is_applicant = True
            # val.username = val.email
            val.save()
            Resume.objects.create(user=val)
            messages.info(request , 'Your account have been created successfully.')
            return redirect('login')
        else:
            print(form.errors)
            messages.error(request , 'Something went wrong.')
            return redirect('register-applicant')
    else:
        form = RegisterForm()
        context = {
            'form': form
        }
    
    return render(request , 'users/register_applicant.html' , context)


# registration of recruiter 
def register_recruiter(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            val = form.save(commit=False)
            val.is_recruiter = True
            val.username = val.email
            val.save()
            Company.objects.create(user=val)
            messages.info(request , 'Your account have been created successfully.')
            return redirect('login')
        else:
            messages.error(request , 'Something went wrong.')
            return redirect('register-recruiter')
    else:
        form = RegisterForm()
        context = {
            'form': form
        }
    
    return render(request , 'users/register_recruiter.html' , context)


# login function 
def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request , username=email , password=password)
        if user is not None and user.is_active:
            login(request , user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Email and password didnt matched.')
            return redirect('login')
    else:
        return render(request , 'users/login.html')
    

# logout user 
def logout_user(request):
    logout(request)
    messages.info(request, 'You have been logged out. Please login to continue.')
    return redirect('login')
            

