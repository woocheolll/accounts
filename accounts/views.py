from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm



def signup(request):
    form = UserCreationForm()
    context = {
        "form": form
        }
    return render(request, 'accounts/signup.html', context)