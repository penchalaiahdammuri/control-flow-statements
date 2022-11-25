from django.shortcuts import render

# Create your views here.
def a2_first(request):
    return render(request,'a2_first.html',context={'a':300,'b':700,'c':500})

def a2_second(request):
    return render(request,'a2_second.html',context={'name':'Penchalaiah'})    