from django.shortcuts import render, redirect


def index(request):
    if 'GET' == request.method:
        return render(request, 'webapp/index.html')
    elif 'POST' == request.method:
        return redirect('dashboard')


def dashboard(request):
    return render(request, 'webapp/dashboard.html')
