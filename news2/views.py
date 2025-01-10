from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def home(request):
    
    return render(request, "news2/home.html",)

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('../admin')
        else:
            return render(request, 'news2/login.html', {'error': 'Invalid username or password'})
    return render (request,"news2/login.html")



def signup(request):
    return render (request, "news2/signup.html",)



def news(request):
    return render(request, "news2/news.html")



def image(request):
    return render(request, "news2/image.html")
