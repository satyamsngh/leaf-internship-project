
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib.auth import login,authenticate

# Create your views here.

def login(request):    
    
    if request.method == 'POST':
        username= request.POST['user']
        password = request.POST['pass']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            return render(request,'index.html')
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')
    

def signup(request):
    if request.method == 'POST':
        user= request.POST['usern']
        password = request.POST['passwd']
        email = request.POST['email1']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        user = User.objects.create_user(username=user, email=email, password=password, first_name=firstname, last_name=lastname) 
        return redirect('index.html')
         
         
    else:
        return render(request,'signup.html')
        
    

def index(request):
    return render(request,'index.html')

def donation(request):
    return render(request,'donation.html')


def forum(request):
    return render(request,'forum.html') 
