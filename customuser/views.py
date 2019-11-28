from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from customuser.models import *
from django.http import JsonResponse, HttpResponseRedirect
from .forms import SignUpForm , UpdateForm

from django.core.mail import send_mail
from django.template.loader import render_to_string



def create_password():
    from random import choices
    import string
    password = ''.join(choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=8))
    return password


def account_edit(request):
    user = request.user
    if request.POST:
        form = UpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return render(request, 'pages/lk.html', locals())
    else:
        userForm = UpdateForm(instance=user)
        return render(request, 'pages/lk.html', locals())




def restore(request):
    return_dict = {}
    return_dict['result'] = False
    try:
        user = User.objects.get(email=request.POST.get('email'))
    except:
        user = None

    if user:
        new_password = create_password()
        user.set_password(new_password)
        user.save()
        return_dict['result'] = True
        msg_html = render_to_string('email/restore_passord.html', {'login': user.email, 'password': new_password})
        send_mail('Новый пароль на сайте LAKSHMI888', None, 'info@lakshmi888.ru', [user.email],
                  fail_silently=False, html_message=msg_html)
    return JsonResponse(return_dict)


def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')


def log_in(request):
    return_dict = {}
    phone = request.POST.get('phone')
    password = request.POST.get('password')
    print(phone)
    user = authenticate(phone=phone, password=password)
    print(user)
    if user is not None:
        if user.is_active:
            login(request, user)
            return_dict['result'] = 'ok'
            return JsonResponse(return_dict)
        else:
            return_dict['result'] = 'inactive'
            return JsonResponse(return_dict)
    else:
        return_dict['result'] = 'invalid'
        return JsonResponse(return_dict)



def signup(request):
    return_dict = {}
    print(request.POST)
    if request.method == 'POST':
        n1 = int(request.POST.get('n1'))
        n2 = int(request.POST.get('n2'))
        answer = int(request.POST.get('answer'))
        if n1 + n2 == answer:
            print(request.POST)
            email = request.POST.get('email')
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            data = {'email': email, 'name': name, 'phone': phone, 'password2': password2, 'password1': password1}
            form = SignUpForm(data=data)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = True
                user.save()
                print('User registred')
                # msg_html = render_to_string('email/register.html', {'login': email, 'password': password1})
                # send_mail('Регистрация на сайте LAKSHMI888', None, 'info@lakshmi888.ru', [email],
                #           fail_silently=False, html_message=msg_html)
                # print('Email sent to {} with pass {}'.format(email,password1))
                login(request, user)


                return_dict['result'] = 'success'
                return JsonResponse(return_dict)
            else:
                return_dict['result'] = form.errors
                print(return_dict)
                return JsonResponse(return_dict)
        else:
            return_dict['result'] = 'bad'
            return JsonResponse(return_dict)

    else:
            form = SignUpForm()
    return_dict['result'] = 'not post'
    return JsonResponse(return_dict)


