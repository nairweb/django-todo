from django.shortcuts import render

# Create your views here.

from core import models

from django.contrib.auth.decorators import login_required
@login_required
def todos(request):
    if request.method=="POST":
        task = request.POST.get("task")
        c = models.todo(task=task)
        c.save()
    mytodo = models.todo.objects.all()
    data = {
        'todos':mytodo
    }
    return render(request,"todo.html",data)

def deleteTodo(request):
    if request.method=="GET":
        todoId = int(request.GET.get("id"))
        models.todo.objects.filter(id=todoId).delete()
    return todos(request)

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
def signup(request):
     if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('/accounts/login')
     else:
        form = UserCreationForm()


     context = {'form': form}
     return render(request, 'signup.html', context)