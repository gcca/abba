from django.shortcuts import render, redirect
from webapp.forms import TeacherForm


def index(request):
    if 'GET' == request.method:
        return render(request, 'webapp/index.html')
    elif 'POST' == request.method:
        return redirect('dashboard')


def dashboard(request):
    return render(request, 'webapp/dashboard.html')


def teacher_form(request):
    form = TeacherForm()
    return render(request, 'webapp/teacher_form.html', { 'form': form })
