from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout, get_user_model, authenticate, login
from .forms import *
import requests
import json
from django.contrib.auth.decorators import login_required


# Create your views here.

# social close form
def close(request):
    # if(request.user.is_authenticated):
    #     login(request)
    # else:
    #     print("hoi")
    return render(request, 'partials/close.html')

# sign-out here.
def signout(request):
    logout(request)
    return redirect('home')

# home views here.
def home(request):
    return render(request, 'users/home.html')

# sign-in here.
def log_in_view(request):
    current_user = request.user
    print(current_user)
    form = LoginForm()
    form2 = Password_Reset_Confirm()
    return render(request, 'validation/login.html', {'form':form, 'form2':form2})

# sign-up proccess here.
def sign_up_view(request):
    form = RegistrationForm()
    return render(request, 'validation/register.html', {'form':form})

# sign-in proccess here.
def log_in_proccess(request):
    data = json.loads(request.POST.get('data'))
    response = requests.post('http://127.0.0.1:8000/api/login/', data)
    if(response.status_code == 200):
        value = json.loads('{"success": "'+data['username']+'"}')
        return HttpResponse(json.dumps(value))
    else:
        return HttpResponse(response)
    
# forgot-password proccess here.
def forgot_password_proccess(request):
    data = json.load(request)['data']
    response = requests.post('http://127.0.0.1:8000/api/reset/sendotp/', data={'email': data})
    return HttpResponse(response)

# forgot-password proccess here.
def forgot_password_confirm_proccess(request):
    data = json.load(request)['TableData']
    response = requests.post('http://127.0.0.1:8000/api/reset/password/', data)
    return HttpResponse(response)

# otp proccess here.
def action_otpsendregistration(request):
    data = json.loads(request.POST.get('data'))
    response = requests.post('http://localhost:8000/api/otp/', data={'email': data})
    if response.status_code == 201:
        return HttpResponse("success")
    else:
        return HttpResponse(response)
    
# sign-up proccess here.
def submit_register(request):
    data = json.loads(request.POST.get('data'))
    response = requests.post('http://127.0.0.1:8000/api/register/', data)
    if response.status_code == 201:
        return HttpResponse(response.status_code)
    else:
        return HttpResponse(response)
    
# home views here.
def user_stats(request):
    return render(request, 'users/home.html')

def watcher(request):
    if(request.user.is_authenticated):
        print(request.user.id)
    else:
        print("hoi")
    return render(request, 'users/home.html')