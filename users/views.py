from django.shortcuts import render, redirect
from .form import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def search(request):
    return render( request ,'search/search.html')

def login(request):
    return render( request, 'login&logout/login.html')

def logout(request):
    return render( request, 'login&logout/logout.html')

def register(request):
     if request.method != "POST":
         form = UserRegisterForm()
         return render(request, 'register/register.html',{'form':form})
     else:
         form = UserRegisterForm(request.POST)
         if form.is_valid():
             form.save()
             username = form.cleaned_data.get('username')
             messages.success(request, f'Account created, Welcome to the cave {username}')
             return redirect('users-search')
      

    

def help(request):
    return render( request, 'help/help.html')


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                    request.FILES, 
                                    instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
            'u_form' : u_form,
            'p_form' : p_form
            }

    return render(request, 'profile/profile.html', context)