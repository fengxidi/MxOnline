#_*_ coding:utf-8 _*_
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password

from .models import UserProfile, EmailVerifyRecord
from .forms import LoginForm,RegisterForm, ForgetPwdForm,ModifyPwdForm
from utils.email_send import send_register_email

# Create your views here.

class ActiveUserView(View):
    def get(self,request,active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email = email)
                user.is_active = True
                user.save()
        else:
            return render(request, 'active_fail.html')

        return  render(request, 'login.html')

        


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html',{'register_form':register_form})
    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = request.POST.get('email', '')
            if UserProfile.objects.filter(username=username):
                return render(request, 'register.html', {'mes':'用户已存在','register_form':register_form})
            else:
                password = request.POST.get('password', '')
                user_profile = UserProfile()
                user_profile.username = username
                user_profile.email = username
                user_profile.is_active = False
                user_profile.password = make_password(password)

                send_register_email(username, 'register')
                user_profile.save()
                return render(request, 'login.html')
        else:
            return render(request, 'register.html', {'register_form':register_form})





class LoginView(View):

    def get(self,request):
        return render(request, 'login.html', {})
    def post(self, request):
        login_form = LoginForm(request.POST)

        #is_valid 验证字段是否合法，
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            #认证username，password
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'index.html')
                else:
                    return  render(request, 'login.html',{'mes':'用户未激活'})
            else:
                return render(request, 'login.html',{'mes': '用户名或密码错误'})
        else:
            return render(request, 'login.html', {'login_form':login_form})


class CustonBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return  None


#已经使用 class LoginView替代
# def user_login(request):
#
#     if request.method == 'POST':
#         user_name = request.POST.get('username', '')
#         pass_word = request.POST.get('password', '')
#         user = authenticate(username=user_name, password= pass_word)
#         if user is not None:
#             login(request, user)
#             return render(request, 'index.html')
#         else:
#             return render(request, 'login.html', {'mes': '用户名或密码错误'})
#     elif request.method == 'GET':
#         return render(request, 'login.html',{})


class ForgetPwdView(View):
    def get(self,request):
        forgetpwd_form = ForgetPwdForm()
        return render(request, 'forgetpwd.html',{'forgetpwd_form':forgetpwd_form})

    def post(self,request):
        forgetpwd_form = ForgetPwdForm(request.POST)

        if forgetpwd_form.is_valid():
            email = request.POST.get('email','')
            send_register_email(email, 'forget')
            return render(request, 'forgetpwd.html', {'success':'邮件发送成功'})

        else:
            return render(request, 'forgetpwd.html', {'forgetpwd_form':forgetpwd_form})

class ResetView(View):
    def get(self,request,reset_code):
        all_records = EmailVerifyRecord.objects.filter(code=reset_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, 'password_reset.html', {'email':email})

        else:
            return render(request, 'active_fail.html')

class ModifyPwdView(View):
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get('password1', '')
            pwd2 = request.POST.get('password2', '')
            email = request.POST.get('email', '')
            if pwd1 != pwd2:
                return render(request, 'password_reset.html', {'email': email, 'mes': '密码不一致'})
            user = UserProfile.objects.get(email=email)
            user.password = make_password(pwd2)
            user.save()
            return render(request, 'login.html',{'success':'密码修改成功'})
        email = request.POST.get('email', '')
        return render(request, 'password_reset.html', {'email': email, 'modify_form': modify_form })


