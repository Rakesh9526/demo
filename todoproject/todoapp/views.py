from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from todoapp.forms import taskform
from todoapp.models import Task
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class tlistview(ListView):
    model = Task
    template_name = "homepage.html"
    context_object_name = 'task1'

class detailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'

class updateview(UpdateView):
    model = Task
    template_name ='update.html'
    context_object_name = 'update'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('dtview',kwargs={'pk':self.object.id})


class deleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbview')



# Create your views here.

def homepg(req):
    task1 = Task.objects.all()
    if req.method=="POST":
        name=req.POST.get('task','')
        priority=req.POST.get('priority','')
        date=req.POST.get('date')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(req,"homepage.html",{'task1':task1})

#
# def showdetail(req):
#
#     return render(req,"detail.html",)

def delete(req,taskid):
    task=Task.objects.get(id=taskid)
    if req.method=="POST":
        task.delete()
        return redirect('/')
    return render(req,"delete.html")

def update(req,upid):
    uptask=Task.objects.get(id=upid)
    f=taskform(req.POST or None,instance=uptask)
    if f.is_valid():
        f.save()
        return redirect("/")
    return render(req,"editpage.html",{'form':f,'task':uptask})
