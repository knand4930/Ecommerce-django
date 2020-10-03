from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, get_user_model
from .forms import ContactForm, LoginForm, RegisterForm
from django.contrib.auth.models import User



# Create your views here.
def login_page(request):
    form = LoginForm(request.POST or None)
    # print(request.user.is_authenticated())
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            form= LoginForm(request.POST or None)
            return redirect('/login')
        else:
            print("error")

    return render(request, 'login_page.html', {'form': form})



User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password )
        print(new_user)
    return render(request, 'register_page.html', {'form': form})



def home_page(request):
    return render(request, 'home_page.html', {})

def about_page(request):
    return render(request, 'about_page.html', {})

    
def contact_page(request):

    contact = ContactForm(request.POST or None)
    if contact.is_valid():
        print(contact.cleaned_data)

    if request.method == 'POST':
        print(request.POST)
    return render(request, 'contact_page.html', {'form': contact})
