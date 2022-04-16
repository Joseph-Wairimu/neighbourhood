from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from .models import NeighborHood,Business,User
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
    profile=User.objects.filter(user=current_user).first()
    return render(request,'profile.html',{"profile":profile})

  