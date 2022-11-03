from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'swiggytemplates/home.html')
def photography(request):
    return render(request,'swiggytemplates/photography.html')
def epanchayath(request):
    return render(request,'swiggytemplates/epanchayath.html')


