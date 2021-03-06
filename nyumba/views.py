from django.shortcuts import render,redirect, get_object_or_404
from .forms import RegisterForm, ProfileUpdateForm,NeighborHoodForm, BusinessForm, PostForm
from django.contrib.auth.decorators import login_required
from .models import NeighborHood,Business,Profile,Post
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

@login_required(login_url='login') 
def add_hood(request):
    current_user=request.user
    if request.method == 'POST':
        form =NeighborHoodForm(request.POST, request.FILES)
        if form.is_valid():
           project = form.save(commit=False)
           project.user = current_user
           project.save()          
        return redirect('hoods')
    else:
            form = NeighborHoodForm()
    return render(request, 'add_hood.html', {"form": form})    

def business(request):   
    business=Business.objects.all()
    return render(request,'business.html',{"business":business})    
    
@login_required(login_url='login') 
def add_business(request):
    current_user=request.user
    if request.method == 'POST':
        form =BusinessForm(request.POST, request.FILES)
        if form.is_valid():
           project = form.save(commit=False)
           project.user = current_user
           project.save()          
        return redirect('business')
    else:
            form = BusinessForm()
    return render(request, 'add_business.html', {"form": form})    

@login_required(login_url='login') 
def joinhood(request, id):
    hood = get_object_or_404(NeighborHood, id=id)
    request.user.profile.NeighborHood = hood
    request.user.profile.save()
    return redirect('hoods')

@login_required(login_url='login') 
def leavehood(request, id):
    hood = get_object_or_404(NeighborHood, id=id)
    request.user.profile.NeighborHood = None
    request.user.profile.save()
    return redirect('hoods')

@login_required(login_url='login') 
def singlehood(request, id):
    hood = NeighborHood.objects.get(id=id)
    return render(request, 'singleNeighborhood.html', {'hood':hood})

def search_business(request):
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_business = Business.search_by_business(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"business": searched_business})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def search_hood(request):
    if 'hood' in request.GET and request.GET["hood"]:
        search_term = request.GET.get("hood")
        searched_hood = NeighborHood.search_by_hood(search_term)
        message = f"{search_term}"

        return render(request, 'searched.html',{"message":message,"hood": searched_hood})

    else:
        message = "You haven't searched for any term"
        return render(request, 'searched.html',{"message":message})        

def post(request):
    current_user=request.user
    if request.method == 'POST':
        form =PostForm(request.POST, request.FILES)
        if form.is_valid():
           project = form.save(commit=False)
           project.user = current_user
           project.save()          
        return redirect('hoods')
    else:
            form = PostForm()
    return render(request, 'post.html', {"form": form})

def single_post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'single_post.html', {'post':post})    

def single_business(request, id):
    business = Business.objects.get(id=id)
   
    return render(request, 'single_business.html', {'business':business})