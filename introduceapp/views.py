from django.shortcuts import render

# Create your views here.
def schedule(request):
    return render(request, 'schedule.html')

def assingment(request):
     return render(request, 'assingment.html')

def introduce(request):
    return render(request, 'introduce.html')
 
def index(request):
    return render(request, 'index.html')