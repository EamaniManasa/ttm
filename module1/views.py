import requests
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
import string
import random

from matplotlib import pyplot as plt

from . import forms
from . forms import IntegerDateForm, PieChartForm

import requests
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.shortcuts import render
import random,datetime
import string
# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

from .forms import *
from .models import*
from django.shortcuts import render,redirect


import matplotlib.pyplot as plt
import numpy as np








# Create your views here.
def hello(request):
    return render(request,'firsthtml.html')
def hello1(request):
    return HttpResponse("<center><font color=blue>Welcome to TTM Homepage</font></center>")
def newhomepage(request):
    return render(request,'newhomepage.html')
def travelpackage(request):
    return render(request,'travelpackage.html')
def print1(request):
    return render(request,'print_to_console.html')
def print_to_console(request):
    if request.method == "POST":
        User_Input= request.POST['User_Input']
        print(f'User_Input:{User_Input}')
    #return HttpResponse('Form Submitted Successfully')
    a1={'User_Input':User_Input}
    return render(request,'print_to_console.html',a1)
def ran(request):
    return render(request,'random123.html')
def random123(request):
    if request.method=='POST':
       input1=request.POST['input1']
       input2=int(input1)
       result_str=''.join(random.sample(string.digits,input2))
       print(result_str)
       context={'result_str':result_str}
    return render(request,"Random123.html",context)

def getdate1(request):
    return render(request,'get_date.html')

import datetime
from django.shortcuts import render
def get_date(request):
    if request.method == 'POST':
        form=IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value=form.cleaned_data['integer_value']
            date_value=form.cleaned_data['date_value']
            updated_date=date_value+datetime.timedelta(days=integer_value)
            return render(request,'get_date.html',{'updated_date':updated_date})
        else:
            form=IntegerDateForm()
        return render(request,'get_date.html',{'form':form})

def tzfunctioncall(request):
    return render(request,'pytzexample.html')

def dataconnection(request):
    return render(request,'data_base.html')

from .models import *
from django.shortcuts import render,redirect
def registerloginfunction(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        phonenumber=request.POST.get('phonenumber')
        if Register.objects.filter(email=email).exists():
            message1="Email already registered.Choose a different email."
            return render(request,'data_base.html',{'message1':message1})
        Register.objects.create(name=name,email=email,password=password,phonenumber=phonenumber)
        return redirect('newhomepage')
    return render(request,'data_base.html')

def pie_chart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            # Process user input
            y_values = [int(val) for val in form.cleaned_data['y_values'].split(',')]
            labels = [label.strip() for label in form.cleaned_data['labels'].split(',')]

            # Create pie chart
            plt.pie(y_values, labels=labels, startangle=90)
            plt.savefig('static/image/pie_chart.png')  # Save the chart image
            img1={'chart_image': '/static/image/pie_chart.png'}
            return render(request, 'picchart.html', img1)
    else:
        form = PieChartForm()
    return render(request, 'picchart.html', {'form': form})

def slidefun(request):
    return render(request,'imgexample.html')

def weathercall(request):
    return render(request,'weather.html')

def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = 'f6ae86e07da82888198d9799b4b6fe81'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1= round(temperature - 273.15,2)
            return render(request, 'weather.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'weather.html', {'error_message': error_message})


def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def login1(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['password']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            return render(request,'newhomepage.html')
        else:
            messages.info(request,'Invalid credentials')
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def signup1(request):
    if request.method=='POST':
       username=request.POST['username']
       pass1=request.POST['password']
       pass2=request.POST['password1']
       if pass1==pass2:
           if User.objects.filter(username=username).exists():
              messages.info(request, 'OOPS! Username already taken')
              return render(request,'signup.html')
           else:
               user=User.objects.create_user(username=username,password=pass1)
               user.save()
               messages.info(request,'Account created Successfully!')
               return render(request,'newhomepage.html')
       else:
           messages.info(request,'Password does not match')
           return render(request,'signup.html')

def logout(request):
    auth.logout(request)
    return render(request,'newhomepage.html')

def contact(request):
    return render(request,'contact.html')

def contactmail(request):
    if request.method=="POST":
        firstname = request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        comment=request.POST['comment']
        tosend=comment + '-----------------------This is just the copy of '
        data = contactus(firstname=firstname,lastname=lastname,email=email,comment=comment)
        data.save()
        return HttpResponse("<h1><center>Thank you giving Feedback</center></h1>")
