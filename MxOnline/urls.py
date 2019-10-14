"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to  For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.generic.base import TemplateView
from django.views.static import serve
from MxOnline.settings import MEDIA_ROOT
#from django.contrib import admin
import xadmin

from users.views import LoginView, RegisterView, ActiveUserView,ForgetPwdView,ResetView,ModifyPwdView
from organization.views import OrgView

urlpatterns = [
    #url(r'^', include('users.urls', namespace='app')),

    #url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^login/$', LoginView.as_view(),  name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    #url(r'^captcha/$', include('captcha.urls')), #错误
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='active_user' ),
    url(r'^forgetpwd/$', ForgetPwdView.as_view(), name='forgetpwd'),
    url(r'^reset/(?P<reset_code>.*)/$', ResetView.as_view(), name='reset'),
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name='modify_pwd'),

    #课程机构首页
    url(r'^org_list/$', OrgView.as_view(), name='org_list'),
    #配置上传文件的访问处理函数
    url(r'media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
]
