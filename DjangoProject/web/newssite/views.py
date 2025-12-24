from django.shortcuts import render,get_object_or_404
from .models import News, Category, Horoscope,Blog


# Create your views here.

def home(request):
    news=News.objects.all()
    categories=Category.objects.all()
    horoscopes = Horoscope.objects.all()
    blogs=Blog.objects.all()
    return render(request,"index.html",{"news":news,"categories":categories,"horoscopes":horoscopes,'blogs':blogs})

def newsDetails(request,news_id):
    news=get_object_or_404(News,pk=news_id)
    categories=Category.objects.all()
    return render(request,'details.html',{'news':news,'categories':categories})

def category(request,category_id):
    category=get_object_or_404(Category,pk=category_id)
    news=News.objects.filter(category=category)
    categories=Category.objects.all()
    return render(request,'category.html',{'category':category,'news':news,'categories':categories})

def about(request):
    categories = Category.objects.all()
    return render(request,"about.html",{"categories":categories})

def contact(request):
    categories=Category.objects.all()
    return render(request,"contact.html",{"categories":categories})

def blog_by_author(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    categories = Category.objects.all()
    return render(request, 'blog_by_author.html', {'blogs': [blog], "categories": categories})
