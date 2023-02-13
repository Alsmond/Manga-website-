from django.shortcuts import render,redirect
from .models import Login,Anime
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        re_password=request.POST.get('repassword')
       
        
        if password==re_password:
            
            messages.success(request,'you have been login successfully')
            a=Login(name=name,email=email,password=password,re_password=re_password)
            a.save()
        
            return redirect('Anime')
        elif password!=re_password:
            messages.error(request,'your password did not match')
            redirect(login)
            
        
        
    return render(request,'login.html')

def anime(request):
    all=Anime.objects.all()
    if request.method=="POST":
        search=request.POST.get("search")
        all=Anime.objects.filter(name__startswith=search)   
    context={'all':all}
    return render(request,'anime.html',context)

def show(request,name):
    anime=Anime.objects.get(name=name)
    for i in anime.files.all():
        print(i)
    context={'anime':anime}
    
    return render(request,"show.html",context)
