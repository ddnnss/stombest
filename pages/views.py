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

def doctor_info(request,id):
    doc = Doctor.objects.get(id=id)
    return render(request, 'doctor.html', locals())

def contact(request):
    return render(request, 'contact.html', locals())

def services(request):
    serv=ServiceCat.objects.all()
    return render(request, 'services.html', locals())

def services_child(request):
    serv = ServiceCat.objects.filter(isChild=True)

    return render(request, 'services_child.html', locals())
def service(request,id):
    serv=ServiceCat.objects.get(id=id)

    return render(request, 'service.html', locals())

def apply(request,id):
    serv=Service.objects.get(id=id)
    months = Month.objects.all()
    days = Day.objects.all()
    times = Time.objects.all()
    docs = Doctor.objects.filter(services=id)

    return render(request, 'apply.html', locals())

def apply_req(request):
    doc=request.GET.get('doc')
    mon = request.GET.get('mon')
    day = request.GET.get('day')
    time = request.GET.get('time')
    service = request.GET.get('service')
    try:
        if doc:
            Apply.objects.create(doc_id=int(doc),client=request.user,service_id=int(service),day_id=int(day),time_id=int(time),month_id=int(mon))
        else:
            Apply.objects.create(client=request.user, service_id=int(service), day_id=int(day),
                                 time_id=int(time), month_id=int(mon))
    except:
        pass
    return HttpResponseRedirect('/')

def update_req(request):
    print(request.POST)
    form = UpdateForm(request.POST, request.FILES, instance=request.user)
    print(form.errors)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/lk')
    else:
        form = UpdateForm()
    return HttpResponseRedirect("/lk")

def login_req(request):
    user = authenticate(username=request.POST.get('phone'), password=request.POST.get('password'))
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

def faq(request):

    return render(request, 'faq.html', locals())

def message(request):
    allmsg = Message.objects.filter(client=request.user)

    return render(request, 'message.html', locals())

def message_add(request):
    Message.objects.create(client=request.user,message=request.GET.get('message'))
    return HttpResponseRedirect('/message')

def lk(request):
    usr=request.user
    docs=Doctor.objects.all()
    form = UpdateForm()
    return render(request, 'lk.html', locals())

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')