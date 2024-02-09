from django.shortcuts import render

# Create your views here. 
def Saturday(requset):
    return render(requset, 'plan/Saturday.html')
def Sunday(requset):
    return render(requset, 'plan/Sunday.html')
def Monday(requset):
    return render(requset, 'plan/Monday.html')
def Tuesday(requset):
    return render(requset, 'plan/Tuesday.html')
def Wednesday(requset):
    return render(requset, 'plan/Wednesday.html')