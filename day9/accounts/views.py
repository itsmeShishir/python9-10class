from django.shortcuts import render

from blog.models import Category
from .forms import UserCreationForm, UserChangeForm, UserChangePassword
# aiuthentication
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'login.html')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        # if  role == admin redirect to admin page and if user == user redirect to home page
        if user is not None:
            login(request, user)
            if user.role == "1":
                return render(request, 'admin/admin.html')
            else :
                return render(request, 'index.html')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

@login_required(login_url='login')    
def logout_user(request):
    logout(request)
    return render(request, 'login.html')

# decorators in django
@login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        form = UserChangePassword(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'change_password.html')
    else:
        form = UserChangePassword()
    return render(request, 'change_password.html', {'form': form})

@login_required(login_url='login')
def change_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return render(request, 'change_profile.html')
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'change_profile.html', {'form': form})

@login_required(login_url='login')
def admin(request):
    # get all the categories
    categories = Category.objects.all()
    print(categories)
    # pass the categories to the template
    context = {
        'categories': categories
    }
    return render(request, 'admins/admin.html', context)