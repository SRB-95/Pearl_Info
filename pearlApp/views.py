from django.shortcuts import render,redirect
from .form import userForm
from django.contrib import messages
from .models import Profile
#login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f"Welcome {username}, You have been successfully registered Please login !")
            form.save()
            return redirect('pearlApp:user_login')
    else:
        form = userForm()
    context = {'form' : form}
    return render(request, 'register.html', context)

def user_login(request):
    if request.method == "POST":
        user_form = AuthenticationForm(request=request, data=request.POST)
        if user_form.is_valid():
            uname = user_form.cleaned_data['username']
            upass = user_form.cleaned_data['password']
            user = authenticate(username = uname, password=upass)
            if user is not None:
                login(request, user)
                # messages.success(request, f"Welcome {uname},You Have Successfully Loggedin to Pearl Info")
                return redirect('pearlApp:user_profile')
    else:
        user_form = AuthenticationForm()
    return render(request, 'user_login.html', {'user_form': user_form})

def user_logout(request):
    logout(request)
    return redirect('pearlApp:home')

@login_required
def about(request):
    return render(request, 'about.html')

@login_required
def contact(request):
    return render(request, 'contact.html')

@login_required
def service(request):
    return render(request, 'service.html')

# @login_required

def add_profile(request):
    user_profile = {}
    if request.method == "GET":
        return render(request, 'add_profile.html')
    elif request.method == "POST":
        email = request.POST['email']
        mob = request.POST['contact']
        place = request.POST['location']
        profile_data = (email, mob, place) 
        user_profile['mail'] = email
        user_profile['contact'] = mob
        user_profile['location'] = place
        print(type(user_profile))
        print(user_profile.get('mail'))
        return render(request, 'user_profile.html', {'user_profile': user_profile})

@login_required
def user_profile(request):
    profile = Profile.objects.all()
    context = {'name': request.user, 'profile': profile}
    return render(request, 'user_profile.html', context)


