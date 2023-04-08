"""界面渲染"""

from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from .models import *

# Create your views here.


# 进入登录界面


def toLogin_view(request):
    return render(request, 'login.html')   # 返回界面


def to_register(request):
    return render(request, 'register.html')


def register_view(request):
    u = request.POST.get("user", '')
    p = request.POST.get("pwd", '')

    if u and p:
        c = StudentInfo.objects.filter(stu_user=u, stu_pwd=p).count()
        if c == 1:
            return HttpResponse("用户存在")
        else:
            return HttpResponse("登录成功")
    else:
        return HttpResponse("请输入账号密码")


def toIndex_view(request):
    u = request.POST.get("user", '')
    p = request.POST.get("pwd", '')

    if u and p:
        c = StudentInfo.objects.filter(stu_user=u, stu_pwd=p).count()
        if c == 1:
            return HttpResponse("登录成功")
        else:
            return HttpResponse("登录失败")
    else:
        return HttpResponse("请输入账号密码")




