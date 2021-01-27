from django.forms import forms
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from app1 import models
from app1.models import User


def login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username', '')
        pass_word = request.POST.get('password', '')
        user = User.objects.filter(username=user_name)  # 查看数据库里是否有该用户名
        if user:  # 如果存在
            user = User.objects.get(username=user_name)  # 读取该用户信息
            if pass_word == user.password:  # 检查密码是否匹配
                request.session['IS_LOGIN'] = True
                request.session['realname'] = user.name
                request.session['username'] = user_name
                return render(request, 'homepage.html', {'user': user}, locals())
            else:
                return render(request, 'login/login.html', {'error': '密码错误!'}, locals())
        else:
            return render(request, 'login/login.html', {'error': '用户名不存在!'}, locals())
    else:
        return render(request, 'login/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        return redirect('/homepage/')
    if request.method == 'POST':
        user_name = request.POST.get('username', '')
        pass_word_1 = request.POST.get('password_1', '')
        pass_word_2 = request.POST.get('password_2', '')
        name = request.POST.get('name', '')
        collage = request.POST.get('collage', '')
        sex = request.POST.get('sex', '')
        classname = request.POST.get('classname', '')
        tel = request.POST.get('tel', '')
        email = request.POST.get('email', '')
        usertype = request.POST.get('usertype', '')
        if User.objects.filter(username=user_name):
            return render(request, 'login/register.html', {'error': '用户已存在'}, locals())
            # 将表单写入数据库
        if pass_word_1 != pass_word_2:
            return render(request, 'login/register.html', {'error': '两次密码请输入一致'}, locals())
        user = User()
        user.username = user_name
        user.password = pass_word_1
        user.tel = tel
        user.classname = classname
        user.collage = collage
        user.email = email
        user.name = name
        user.sex = sex
        user.usertype = usertype
        user.save()
        # 返回注册成功页面
        return redirect('login/login.html')
    else:
        return render(request, 'login/register.html', locals())


def logout(request):
    return redirect('login/')


def index(request):
    return render(request, 'index.html', locals())


def homepage(request):
    if request.session.get('is_login', None):
        return redirect('/index/')
    else:
        return render(request, 'homepage.html')


def forget_password(request):
    if request.method == 'POST':
        user_name = request.POST.get('username', '')
        email = request.POST.get('email', '')
        user = User.objects.filter(username=user_name)
        if user:
            user = User.objects.get(username=user_name)
            if user.email == email:
                request.session['user_name'] = user_name
                return render(request, 'login/reset.html')
            else:
                return render(request, 'login/forget.html', {'error': '您的用户名和邮箱不匹配！'})
        else:
            return render(request, 'login/forget.html', {'error': '请输入正确的用户名'})
    else:
        return render(request, 'login/forget.html')


def reset(request):
    if request.method == 'POST':
        pass_word1 = request.POST.get('password1', '')
        pass_word2 = request.POST.get('password2', '')
        user_name = request.session['user_name']
        user = User.objects.get(username=user_name)
        if pass_word1 == pass_word2:
            user.password = pass_word1
            user.save()
            return render(request, 'login/login.html')
        else:
            return render(request, 'login/reset.html', {'error': '两次密码输入不一致！'})
    else:
        return render(request, 'login/reset.html')


def personpage(request):
    return render(request, 'personpage.html', locals())


def topic(request):
    return None


def management(request):
    usertype = models.User.objects.filter(name='usertype')
    if usertype == 'teacher':
        return render(request, 'management.html')
    else:
        return render(request, 'homepage.html')


def topics(request):
    return render(request, 'topics.html')
