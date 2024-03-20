from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

def users(request):
    item_list = User.objects.order_by("-fullname", "-password")
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = UserForm()

    context = {
		"forms": form,
		"list": item_list,
		"title": "User list",
	}
    return render(request, 'user.html', context)

def user_login(request):
    if request.method == "POST":
        fullname = request.POST['fullname']
        password = request.POST['password']
        user = authenticate(request, fullname=fullname, password=password)

        if user is not None:
            login(request, user)
            return redirect('test_1')
        else:
            return render(request, 'log_in.html',
                          context={"error_message": 'invalid login'})

    return render(request, 'log_in.html')

def tests_1(request):
    return render(request, 'test_sheet.html')

def t(request):
    if request.method == 'POST':
        if 'set_button' in request.POST:
            malumot = request.POST.get('data', '')
            print(malumot)

            if len(malumot) != 0:
                Malumot.objects.create(data=malumot)

            return render(request, 't1.html')

    else:
        return render(request, 't1.html')

def t2(request):
    if request.method == 'POST':
        if 'set_button' in request.POST:
            malumot = request.POST.get('data', '')
            print(malumot)

            if len(malumot) != 0:
                Malumot.objects.create(data=malumot)

            return render(request, 't2.html')

    else:
        return render(request, 't2.html')

def t3(request):
    if request.method == 'POST':
        if 'set_button' in request.POST:
            malumot = request.POST.get('data', '')
            print(malumot)

            if len(malumot) != 0:
                Malumot.objects.create(data=malumot)

            return render(request, 't3.html')

    else:
        return render(request, 't3.html')

def t4(request):
    if request.method == 'POST':
        if 'set_button' in request.POST:
            malumot = request.POST.get('data', '')
            print(malumot)

            if len(malumot) != 0:
                Malumot.objects.create(data=malumot)

            return render(request, 't4.html')

    else:
        return render(request, 't4.html')

def t5(request):
    if request.method == 'POST':
        if 'set_button' in request.POST:
            malumot = request.POST.get('data', '')
            print(malumot)

            if len(malumot) != 0:
                Malumot.objects.create(data=malumot)

            return render(request, 't5.html')

    else:
        return render(request, 't5.html')

def t6(request):
    if request.method == 'POST':
        if 'set_button' in request.POST:
            malumot = request.POST.get('data', '')
            print(malumot)

            if len(malumot) != 0:
                Malumot.objects.create(data=malumot)

            return render(request, 't6.html')

    else:
        return render(request, 't6.html')

def ex(request):
    context = {
        'other':'https://www.w3schools.com'
    }
    return render(request, 'exit.html', context)


def test_ansver(request):
    if Answer.answ == Malumot.data:
        context = {
            'true':Answer.objects.all(),
            'false':Malumot.objects.all(),
            'title':'Answer sheet',
            'Anw':'You choose true answers'
        }
        return render(request, 'answer.html', context)
    elif Answer.answ != Malumot.data:
        context = {
            'true':Answer.objects.all(),
            'false':Malumot.objects.all(),
            'title':'Answer sheet',
            'Anw':'You have had mistakes'
        }
        return render(request, 'answer.html', context)


