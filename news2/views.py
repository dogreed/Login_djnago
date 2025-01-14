from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from .models import AddNews 


def home(request):
    return render(request, "news2/home.html",)


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/adminmain/')
        else:
            return render(request, 'news2/login.html', {'error': 'Invalid username or password'})
    return render (request,"news2/login.html")



def news(request):
     news_items = AddNews.objects.all().order_by('-id')  # You can change the order as needed

    # Pass the news items to the template
     return render(request, "news2/news.html", {'news_items': news_items})



def image(request):
    return render(request, "news2/image.html")

# for adimin 


def addnews(request):

    if request.method == 'POST':  # Form was submitted
        title = request.POST.get('title')
        description = request.POST.get('description')       
        image = request.FILES.get('image')

        

        # Save news to the database
        AddNews.objects.create(
            title=title,
            description=description,
            image=image,
            
        )

        return redirect('/addnews')  

    news_items = AddNews.objects.all()
    return render(request, 'news2/admin/addnews.html', {'news_items': news_items})



def admin(request):
    return render(request, "news2/admin/admin.html",)



# delete news 
def delete_news(request, news_id):
    # Fetch the news item or return 404 if not found
    news_item = get_object_or_404(AddNews, id=news_id)

    # Delete the news item
    news_item.delete()

    # Redirect back to the news list page
    return redirect('addnews')
