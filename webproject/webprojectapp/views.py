from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Place
from .models import Team


# Create your views here.
def fun1(request):
    place = Place.objects.all()
    team = Team.objects.all()
    return render(request, 'index.html', {'result1': place, 'result2': team})


def register(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        firstname = request.POST['first_name']
        secondname = request.POST['last_name']
        email = request.POST['email']
        pwrd = request.POST['password']
        cpwrd = request.POST['cpassword']
        if pwrd == cpwrd:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already exist')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already exist')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=firstname, last_name=secondname,
                                                email=email,
                                                password=pwrd)
                user.save()
                messages.info(request, 'registered successfully')
                return redirect('login')
        else:
            messages.info(request,'Password is not matching')
            return redirect('register')
        return redirect('/')
    return render(request, template_name='register.html')


def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credential')
            return redirect('login')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
