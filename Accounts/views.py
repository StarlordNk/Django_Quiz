from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def signup(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['Email']
        password=request.POST['password']
        dob=request.POST['dob']
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username Exists')
            return redirect('signup')
        if User.objects.filter(email=email).exists():
            messages.info(request,'Email duplicate ')
            return redirect('signup')
        else:
            user=User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
            user.save();
            m=Marks.objects.create(fk=user.id,score=0)
            messages.info(request,'User created')
            return redirect('/')
    else:
        return render(request,'signup.html')


def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid Username or Password')
            return redirect('login')
    else:
        
        return render(request, 'login.html')