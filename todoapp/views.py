from todoapp.forms import RegisterUserForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from todoapp.models import Task, Todo
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_todo(sender, instance, created, **kwargs):
    if created:
        Todo.objects.create(user=instance) 
    
# Create your views here.
def registration(request):
    form = RegisterUserForm()
    context = {'form' : form}
    return render(request, 'register.html', context)

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)
            
            return redirect('home')
        else:
            form = RegisterUserForm()
            print(form.errors)
            context = {'form' : form}
            return render(request, 'register.html', context)

def login_page(request):
    logout(request)
    return render(request, 'login.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.add_message(request, messages.INFO, "You're not yet registered or you may have entered an incorrect password.")
            return redirect('register')
    else:
        return redirect('login')

def home(request):
    tasks = Task.objects.filter(todo=request.user.todo)
    for task in tasks:
        print(task)
    context = {'tasks' : tasks}
    return render(request, 'home.html', context)

def add_task(request):
    if request.method == "POST":
        new_task = request.POST['task']
        task = Task.objects.create(task=new_task, todo=request.user.todo)
        task.save()

        return redirect('home')

    else:
        return redirect('home')

def delete_task(request, pk):
    if request.method == "POST":
        task = Task.objects.filter(pk=pk)
        task.delete()

        return redirect('home')

def logout_user(request):
    logout(request)
    return redirect('login')
    