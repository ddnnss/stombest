import json

from django.http import HttpResponseRedirect, JsonResponse
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
    msg = Message.objects.last()

    return render(request, 'index.html', locals())

def doc(request):
    docs=Doctor.objects.all()

    return render(request, 'doctors.html', locals())

def doctor_info(request,id):
    doc = Doctor.objects.get(id=id)

    return render(request, 'doctor.html', locals())

def contact(request):
    contactInfo = Contact.objects.first()
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
    serv=SubService.objects.get(id=id)
    cat = serv.category.category.all()
    print(cat)
    months = Month.objects.all()
    days = Day.objects.all()
    times = Time.objects.all()
    docs = Doctor.objects.filter(services__in=cat)
    print(docs)

    return render(request, 'apply.html', locals())
def apply_default(request):
    serv=Service.objects.all()
    print(serv.filter(id=14))
    print(Doctor.objects.filter(services__in=serv.first().category.all()))
    subservice = SubService.objects.all()
    months = Month.objects.all()
    days = Day.objects.all()
    # times = Time.objects.all()
    # docs = Doctor.objects.all()

    return render(request, 'apply_default.html', locals())
def apply_req(request):
    print(request.GET)
    doc=request.GET.get('doc')
    mon = request.GET.get('mon')
    day = request.GET.get('day')
    # time = request.GET.get('time')
    service = request.GET.get('service')
    comment = request.GET.get('comment')
    try:
        if doc != '0':
            print('doc yes')
            Apply.objects.create(doc_id=int(doc),client=request.user,service_id=int(service),day_id=int(day),comment=comment,month_id=int(mon))
        else:
            print('doc no')
            Apply.objects.create(client=request.user, service_id=int(service), day_id=int(day),
                                 comment=comment, month_id=int(mon))
    except:
        pass
    return HttpResponseRedirect('/')

def apply_default_req(request):
    print(request.GET)
    doc=request.GET.get('doc')
    mon = request.GET.get('mon')
    day = request.GET.get('day')
    # time = request.GET.get('time')
    service = request.GET.get('service')
    comment = request.GET.get('comment')
    try:
        if doc != '0':
            print('doc yes')
            Apply.objects.create(doc_id=int(doc),client=request.user,servicee_id=int(service),day_id=int(day),comment=comment,month_id=int(mon))
        else:
            print('doc no')
            Apply.objects.create(client=request.user, servicee_id=int(service), day_id=int(day),
                                 comment=comment, month_id=int(mon))
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
    all_faq = Faq.objects.all()

    return render(request, 'faq.html', locals())

def message(request):
    allmsg = Message.objects.filter(client=request.user)
    try:
        msg = Message.objects.last()
        if msg.answer:
            msg.isRead = True
            msg.save()
    except:
        pass
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

def get_doc(request):
    body = json.loads(request.body)
    return_dict = {}
    print(body)
    serv = Service.objects.get(id=body['id'])
    print(serv)
    print(Doctor.objects.filter(services__in=serv.category.all()))
    return_dict['docs'] = list()
    docs = Doctor.objects.filter(services__in=serv.category.all())
    for doc in docs:
        return_dict['docs'].append({'id': doc.id,
                                             'name': doc.name})
    return JsonResponse(return_dict)