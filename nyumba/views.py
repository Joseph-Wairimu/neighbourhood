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
def profile(request):
    current_user=request.user
    profile=Profile.objects.filter(user=current_user).first()
    return render(request,'profile.html',{"profile":profile})

def edit_profile(request):
    current_user=request.user
    profile=Profile.objects.filter(user=current_user).first()
    if request.method == 'POST':
        form =  ProfileUpdateForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form =  ProfileUpdateForm(instance=profile)
    return render(request,'edit_profile.html',{"form":form})
  