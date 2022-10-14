from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django.contrib.auth import get_user_model



def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # ModelForm의 save 메서드의 리턴값은 해당 모델의 인스턴스다!
            auth_login(request, user) # 로그인
            return redirect('accounts:index')
    else:   
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == 'POST':
        # AuthenticationForm은 ModelForm이 아님!
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'accounts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def index(request):
    users = User.objects.all()
    # Template에 전달한다.
    context = {"users": users}
    return render(request, "accounts/index.html", context)

def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {
        'user': user
    }
    return render(request, 'accounts/detail.html', context)