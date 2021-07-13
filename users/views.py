from django.shortcuts import render, redirect
from .form import UserRegisterForm
from django.contrib import messages

# Create your views here.
def search(request):
    return render( request ,'search/search.html')

def login(request):
    return render( request, 'login&logout/login.html')

def logout(request):
    return render( request, 'login&logout/logout.html')

def register(request):
     if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}, Welcome to the Cave :)')
            return redirect('user-search')
        else:
            form = UserRegisterForm()
        return render(request, 'register/register.html',{'form':form})
    

def help(request):
    return render( request, 'help/help.html')