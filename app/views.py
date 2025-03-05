from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from app.models import *
# Create your views here.

def home(request):
    all_todos=Todo.objects.all()
    d={'all_todos':all_todos}
    if request.method=='POST':
        title=request.POST.get('title')
        desc=request.POST.get('desc')
        to=Todo(title=title,desc=desc)
        to.save()
    return render(request,'home.html',d)

def update(request,pk):
    to=Todo.objects.get(pk=pk)
    d={'to':to}
    if request.method=='POST':
        title=request.POST.get('title')
        desc=request.POST.get('desc')
        to.title=title
        to.desc=desc
        to.save()
        return HttpResponse(reverse('home'))
    return render(request,'update.html',d)

def delete(request,pk):
    to=Todo.objects.get(pk=pk)
    to.delete()
    return HttpResponse(reverse('home'))