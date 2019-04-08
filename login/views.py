from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from . import forms
# redirct用于logout后。重定向到'index'首页
# Create your views here.

def index(request):
    pass
    return render(request, 'login/index.html')


# def login(request):
#     if request.session.get('is_login', None):
#         return redirect("/index/")
#     if request.method == "POST":
#         login_form = forms.UserForm(request.POST)
#         message = "请检查填写的内容！"
#         if login_form.is_valid():
#             username = login_form.cleaned_data['username']
#             password = login_form.cleaned_data['password']
#             try:
#                 user = models.User.objects.get(name=username)
#                 if user.password == password:
#                     request.session['is_login'] = True
#                     request.session['user_id'] = user.id
#                     request.session['user_name'] = user.name
#                     return redirect('/index/')
#                 else:
#                     message = "密码不正确！"
#             except:
#                 message = "用户不存在！"
#         return render(request, 'login/login.html', locals())
#
#     login_form = forms.UserForm()
#     return render(request, 'login/login.html', locals())

def login(request):
    if request.session.get('is_login', None):
        return redirect("/index/")
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        message = "请检查填写的内容"
        if username and password:  # 确保用户名和密码都不为空
            username = username.strip()
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在！"
        return render(request, 'login/login.html', {"message": message})
    return render(request, 'login/login.html')



def register(request):
    pass
    return render(request, 'login/register.html')


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/index/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/index/")