from django.shortcuts import render

# Create your views here.
def myportfolio(request):
    return render(request,'portfolio.html')
def details(request):
    return render(request,'details.html')
def education(request):
    return render(request,'education.html')
def personal(request):
    return render(request,'personal.html')
def certification(request):
    return render(request,'certification.html')