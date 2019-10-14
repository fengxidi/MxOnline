# _*_ coding: utf-8 _*_
__auther__ = 'guozheng'
__date__ = '2019-10-14 9:23'

from django import forms
from operation.models import UserAsk

# class UserAskForm(forms.Form):
#     name = forms.CharField(required=True, min_length=2, max_length=20)
#     mobile = forms.CharField(required=True, min_length=11, max_length=11)
#     course_name = forms.CharField(required=True, min_length=3, max_length=30)

class AnotherUserForm(forms.ModelForm):

    #可添加字段

    class Meta:
        #指明model
        model = UserAsk()
        #指明字段
        fields = ['name', 'mobile', 'course_name']