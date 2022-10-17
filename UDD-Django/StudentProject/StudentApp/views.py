from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from StudentApp.models import Student
# Create your views here.
def index(request):
    return render(request,"index.html")

def all(request):
    stu = Student.objects.all()
    return render(request,"all.html",{'stu':stu})

def create(request):
    if request.method == 'POST':
        ID = request.POST['id']
        name = request.POST['name']
        email = request.POST['email']
        phone =request.POST['phone']
        std = request.POST['std']
        sec = request.POST['sec']
        roll = request.POST['roll']
        Student(ID=ID, name=name, email=email, phone=phone, std=std, sec=sec, roll=roll).save()
       
    return render(request,"create.html")
