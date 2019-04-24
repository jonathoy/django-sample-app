from django.shortcuts import render

def index(request):
    return render(request, 'mentorfinder/index.html')
