from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse('This is my home page (/)')
    context ={'fname':'Chetan', 'lname':'Tewari'}
    return render(request,'home.html', context)
def about(request):
    #return HttpResponse('This is my about page (/about)')  
    return render(request,'about.html')
def projects(request):
    #return HttpResponse('This is my project page (/projects)')
    return render(request,'projects.html')
def contact(request):
    #return HttpResponse('This is my home page (/contact)')
    return render(request,'contact.html')