from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render,redirect
from onlineschool.forms import *
from onlineschool.models import Student
from django.contrib.auth import login,logout,authenticate
from django.utils.decorators import method_decorator

# Create your views here.



def sigin_required(func):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return func(request,*args,**kwargs)
        else:
            return redirect('login')
    return wrapper
class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{'forms':form})
    def post(self,request):
        form=LoginForm(request.POST)
        if form.is_valid():
            usera=form.cleaned_data.get('username')
            pas=form.cleaned_data.get('password')
            print(usera,pas)
            user=authenticate(username=usera,password=pas)
            print(user)
            if user:
                login(request,user)
                return redirect("home")
            else:
                return render(request, "login.html", {'forms': form})

        else:
            return render(request, "login.html", {'forms': form})


class Home(View):

    def get(self,request,*args,**kwargs):
        return render(request,"schoolhome.html")

def Logout(request,*args,**kwargs):
    logout(request)
    return redirect("login")


class StudentView(View):
    def get(self,request,*args,**kwargs):
        form=StudentForm()
        return render(request,"studentappadd.html",{"forms":form})

    def post(self, request, *args, **kwargs):
        form=StudentForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "studentappadd.html", {"forms": form})

        else:
            return render(request, "studentappadd.html", {"forms": form})



# def listAll( *args, **kwargs):
#         students=Student.objects.all()
#         print("Students :",students)
#         form = StudentForm()
@method_decorator(sigin_required,name='dispatch')

def remove(request,*args,**kwargs):
    id=kwargs.get('sid')
    student=Student.objects.get(id=id)
    student.delete()
    Students=Student.objects.all()
    return render(request,'studentall.html',{'students':student})

class IdeCreateView(View):
    def get(self,request,*args,**kwargs):
        form=IdForm()
        return render(request,'idregister.html',{'forms':form})
    def post(self,request,*args,**kwargs):
        form=IdForm(request.POST)
        if form.is_valid():
            form.save()
        form=IdForm()
        return render(request,'idregister.html',{'forms':form})
class PersonCreateView(View):
    def get(self,request,*args,**kwargs):
        form=PersonForm()
        return render(request,'idregister.html',{'forms':form})
    def post(self,request,*args,**kwargs):
        form=PersonForm(request.POST)
        if form.is_valid():
            form.save()
        form=PersonForm()
        return render(request,'idregister.html',{'forms':form})
class EnrollView(View):
    def get(self,request,*args,**kwargs):
        form=EnrollForm()
        return render(request,'enrollregister.html',{'forms':form})
    def post(self,request,*args,**kwargs):
        form=EnrollForm(request.POST)
        if form.is_valid():
            form.save()
        form=EnrollForm()
        return render(request,'enrollregister.html',{'forms':form})
    def listAll(request,*args,**kwargs):
        enrolls=Enroll.objects.all();
        return render(request, 'enrolllist.html', {'enrolls': enrolls})
