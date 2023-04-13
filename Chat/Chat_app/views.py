from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views import View
# Create your views here.
class loginview(View):
    def get(self, request):
        return render(request, 'user/login.html')
    def post(self, request):
        username= request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Logged In!")
            print(user)
            return redirect('body')

class register(View):
    def get(self, request):
        return render(request, 'user/register.html')
    def post(self, request):
        username=request.POST.get('username')
        password=request.POST.get('password')
        email= request.POST.get('email')
        user = User.objects.create_user(username=username, password=password, email=email)
        messages.success(request, "User Created!")
        return redirect('login')
    
class logoutview(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Logged out!')
        return redirect('login')


class chat_body(View):
    def get(self, request):
        return render(request, 'media/chat_body.html')
    def post(self, request):
        message= request.POST.get('message')
        return render(request, 'media/chat_body.html')