from django.shortcuts import render

# Create your views here.
def a1_first(request):
    return render(request,'a1_first.html',context={'a':101,'b':200})

def a1_second(request):
    return render(request,'a1_second.html',context={'a':1000,'b':150,'c':200})