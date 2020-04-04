from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
from home.models import Register
from django.contrib.auth.models import User,auth
# Create your views here.
def index(request):
	return render(request, 'index.html')

# Signup general
def register(request):
	if request.method=="POST":
		username = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('password')
		#user = authenticate(username=username,password=password)
		#if User.objects.filter(username=username).exits():
		#	return render(request, 'register.html')
		
		register = Register(username=username, email=email, password=password)
		register.save()
			#login(request,register)
		return render(request, 'index.html', {'username':username})

	return render(request, 'register.html')
