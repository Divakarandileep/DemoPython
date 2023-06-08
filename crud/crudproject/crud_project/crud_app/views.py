from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from . models import Task
from  django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView


# Create your views here.
def demo(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        num=request.POST.get('num','')
        name=request.POST.get('name','')
        decription=request.POST.get('decription','')
        task=Task(num=num,name=name,decription=decription)
        task.save()
        messages.success(request, "Data saved Succesfully")
        return render('/')
    return render(request,'home.html',{'task1':task1})

def delete (request,id):
    task=Task.objects.get(id=id)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')
    # return render(request,'delete.html')

# def update(request,id=id):
#     updt=Task.objects.get(id=id)
#     if request.method=='POST':
#         updt.save()
#         return redirect('/')
#     return render(request,'update.html')


def update(request, id):
    contact1 = Task.objects.all()
    contact = Task.objects.get(id=id)

    if request.method == 'POST':
        num = request.POST.get('num', '')
        name = request.POST.get('name', '')
        decription = request.POST.get('decription', '')

        contact.num = num
        contact.name = name
        contact.decription = decription
        contact.save()
        messages.success(request, "Data updated  Succesfully")

        return redirect('/')

    return render(request, 'update.html', {'contact1': contact1, 'contact': contact})



# def update(request, id):
#     Task = get_object_or_404( id=id)
#     if request.method == 'POST':
#         data = request.POST
#         Task.sino=data.get('num')
#         Task.name = data.get('name')
#         Task.description = data.get('decription')
#         # Update more fields as needed
#         Task.save()
#         messages.info(request, "UPDATED SUCCESSFULLY!")
#         return redirect('crud')
#
#     context = {
#         'Task': Task
#     }
#     return render(request, 'update.html', context)