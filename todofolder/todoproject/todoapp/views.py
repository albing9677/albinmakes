from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def add(request):
    taskobj = Task.objects.all
    if request.method=='POST':
        name=request.POST.get('name','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(name=name,priority=priority,date=date)
        task.save()
        taskobj = Task.objects.all
    return render(request,'home.html',{'taskobj':taskobj})

def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')



