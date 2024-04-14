# from django.http import HttpResponse
from  django.shortcuts import render
from blog.models import Post,Category

def home(request):
    posts=Post.objects.all()[:11]
    
    category=Category.objects.all()
    
    data={
        "posts":posts,
        "category":category,
    }
    for i in posts:
        print(i.content)
    return render(request,'home.html',data)

def post(request,url):
    post=Post.objects.get(url=url)
    category=Category.objects.all()
    data={
        "post":post,
        "category":category,
    }
    return render(request,'post.html',data)

def category(request,url):
    cat=Category.objects.get(url=url)
    posts=Post.objects.filter(cat=cat)
    data={
        "posts":posts,
        "cat":cat,
    }
    return render(request,"category.html",data)


def contact(request):
    return render(request,"contact.html")