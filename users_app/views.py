from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm # Helper to create defaul forms in DJANGO. 
from django.contrib import messages
from .forms import CustomRegisterForm

def register(request):
    if request.method == "POST":
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid(): # If the information in request.POST is valid, do all the following.
            register_form.save() # Save the register account in database.
            messages.success(request, ("New User Account Created, Login To Get Started!")) # If register_form is valid, show a success message.
            return redirect('register')
    else: # If the request is a "GET", do all the following.
        register_form = CustomRegisterForm()
    return render(request, 'register.html', {'register_form': register_form})
