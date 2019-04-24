from django.shortcuts import render

def index(request):
    return render(request, 'mentorfinder/index.html')

def create(request):
    return render(request, 'mentorfinder/create.html')
