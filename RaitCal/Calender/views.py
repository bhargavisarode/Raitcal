from django.shortcuts import render, HttpResponse, redirect

def login(request):

    return render(request, 'logintypes.html')

def logintype(request):

    return render(request, 'loginpage.html')

def register(request):

    return render(request, 'register.html')
