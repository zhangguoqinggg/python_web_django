"""
专门存放函数的文件
"""
from django.shortcuts import HttpResponse,render,redirect
from django import forms

class RegForm(forms.Form):
    def clean(self):
        pass

def index(request):
    return render(request,"index.html")

def login(request):
    error_msg = ''
    if request.method =='POST':
        email = request.POST['email']
        pwd = request.POST['pwd']
        if email == 'zgq' and pwd == 'zgq':
            return redirect('/index/')
        else:
            error_msg = '用户名或密码错误！！！'
    return render(request,"login.html" ,{'error_msg':error_msg})