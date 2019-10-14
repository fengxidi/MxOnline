# _*_ coding: utf-8 _*_
__auther__ = 'guozheng'
__date__ = '2019-10-14 16:11'

from django.conf.urls import url, include
from django.views.generic.base import TemplateView
from django.views.static import serve
from MxOnline.settings import MEDIA_ROOT
from .views import OrgView

urlpatterns = [
    #课程机构首页
    url(r'^org_list/$', OrgView.as_view(), name='org_list'),
    #配置上传文件的访问处理函数
    url(r'media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),


]
