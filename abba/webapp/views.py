from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hola todo el mundo ahI fuera que usa MINIX...')
