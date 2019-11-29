from django.http import HttpResponseRedirect
from django.shortcuts import render
from customuser.forms import *
from .models import *



from customuser.forms import *
from django.contrib.auth import authenticate,logout,login

def index(request):
    if request.user.is_authenticated:
        apply = Apply.objects.filter(client=request.user)
    banner = Banner.objects.all()
    loginform = SignUpForm()
    return render(request, 'index.html', locals())

def doc(request):
    docs=Doctor.objects.all()

    return render(request, 'doctors.html', locals())

def services(request):
    serv=Service.objects.all()

    return render(request, 'services.html', locals())
def service(request,id):
    serv=Service.objects.get(id=id)

    return render(request, 'service.html', locals())

def login_req(request):
    user = authenticate(username=request.POST.get('email'), password=request.POST.get('password'))
    if user is not None:
        login(request, user)
        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect('/')

def reg_req(request):
    print(request.POST)

    data = request.POST.copy()

    form = SignUpForm(data)

    if not form.errors:
        new_user = form.save(data)
        login(request, new_user)
        return HttpResponseRedirect("/lk")
    else:
        print(form.errors)


    return HttpResponseRedirect("/")

def todoc(request):
    Apply.objects.create(doc_id=request.GET.get('doc'), client=request.user)
    return HttpResponseRedirect('/')




def lk(request):
    docs=Doctor.objects.all()

    return render(request, 'lk.html', locals())