from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from .models import *

def register(request):
    if request.method == 'POST':
        u = User.objects.create_user(
            username=request.POST.get('l'),
            password=request.POST.get('p')
        )
        Student.objects.create(
            fullname = request.POST.get('fl'),
            guruh = request.POST.get('g'),
            st_raqam = request.POST.get('st'),
            tel = request.POST.get('t'),
            user = u
        )
        return redirect('/')
    return render(request, 'register.html')


def todo(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            Todo.objects.create(
                nom=request.POST.get('nomi'),
                vaqt=request.POST.get('vaqti'),
                tarixi=request.POST.get('tarix'),
                stats=request.POST.get('status'),
                student=Student.objects.get(user=request.user)
            )
            return redirect('/todo/')

    ktb = {
        'habarlar': Todo.objects.filter(student__user=request.user)
    }

    return render(request, 'todo.html', ktb)


def todoni_ochir(request,son):
    if Todo.objects.get(id=son).student.user == request.user:
        Todo.objects.get(id=son).delete()
        return redirect('/todo/')

def todoni_tahrirlash(request, son):
    if request.method == 'POST':
        if request.POST.get('status') == 'on':
            natija = False
        else:
            natija = True
        Todo.objects.filter(id=son).update(
            nom=request.POST.get('nomi'),
            vaqt=request.POST.get('vaqti'),
            tarixi=request.POST.get('tarix'),
            stats=natija,

        )
        return redirect('/todo/')
    data = {
        'h':Todo.objects.get(id=son)
    }

    return render(request, 'todo_edit.html', data)


def loginView(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('l'),password=request.POST.get('p'))
        if user is None:
            return redirect('/')
        login(request, user)
        return redirect('/todo/')
    return render(request, 'login.html')

def logoutView(request):
    logout(request)
    return redirect('/')



