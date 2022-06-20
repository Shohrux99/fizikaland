from django.shortcuts import render

# Create your views here.


def IndexView(request):

    return render(request,'main/index.html')

def first(request):

    return render(request,'main/1.html')

def second(request):

    return render(request,'main/2.html')

def third(request):

    return render(request,'main/3.html')

def fourth(request):

    return render(request,'main/4.html')

def fifth(request):

    return render(request,'main/5.html')