from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import EmployeeRoles
from . import forms

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        result = []
        query = EmployeeRoles.objects.filter(user=request.user)
        for i in query:
            result.append({
                'organisation': i.organisation.name,
                'role': i.role.name
            })
        return render(request, 'home.html', context={'username': request.user, 'data': result})
    else:
        return redirect('/login/?next=%s' % request.path)

def login_page(request):
    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/', permanent=True)
            else:
                return render(request, 'login.html', context={'form': form, 'error': 'Invalid credentials'})
    return render(request, 'login.html', context={'form': form})
    
def logout_page(request):
    logout(request)
    return redirect('/', permanent=True)