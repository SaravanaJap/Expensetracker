from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required

from .models import Account
# Create your views here.

def register(request):
    print(request.method)
    if request.method == 'POST':

        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            print(first_name)
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            username = email.split("@")[0]
            password = form.cleaned_data['password']
            

            user = Account.objects.create_user(first_name = first_name,last_name = last_name,email=email,password=password,username=username)
            user.is_active=True 
            user.save()
            
            messages.success(request,'Registration successful')
            return redirect('register')
        else:
            print("not valid")
    else:     
        form = RegistrationForm()
    context = { 
        'form':form,
    }
    return render(request,'accounts/register.html',context)

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email,password = password)
        print(user)

        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.error(request,'Invalid login credentials')
            return redirect('login')
    return render(request,'accounts/login.html')


@login_required( login_url= 'login')
def logout(request):
    auth.logout(request)
    messages.success(request,"You are logged out.")
    return redirect('login')
    