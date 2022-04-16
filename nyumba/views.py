from django.shortcuts import render,redirect
from .forms import RegisterForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .models import NeighborHood,Business,Profile
# Create your views here.
def index(request):
    return render(request, 'index.html')



def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():

            form.save()
           
            
            return redirect('login')
    else:
        form = RegisterForm()
    return render(response, 'register/register.html', {'form': form})  

@login_required(login_url='login')     
def profile(request):
    current_user=request.user
    profile=Profile.objects.filter(user=current_user)
    return render(request,'profile.html',{"profile":profile})

@login_required(login_url='login') 



@login_required(login_url='login') 
def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form =ProfileUpdateForm(request.POST, request.FILES)
        if form.is_valid():
           project = form.save(commit=False)
           project.user = current_user
           project.save()          
        return redirect('profile')
    else:
            form = ProfileUpdateForm()
    return render(request, 'edit_profile.html', {"form": form})
def hoods(request):
    hoods=NeighborHood.objects.all()
    return render(request,'hoods.html',{"hoods":hoods}) 