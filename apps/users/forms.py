# _*_ coding: utf-8 _*_
__auther__ = 'guozheng'
__date__ = '2019-10-3 22:08'

from django import forms
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)

class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=6)
    captcha = CaptchaField(error_messages={"invalid":u'验证码错误'})

class ForgetPwdForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid":u'验证码错误'})

class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True,min_length=6)
    password2 = forms.CharField(required=True, min_length=6)


