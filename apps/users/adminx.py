# _*_ coding: utf-8 _*_
__auther__ = 'guozheng'
__date__ = '2019-10-1 16:28'


import xadmin
from xadmin import views

from .models import EmailVerifyRecord, Banner

class BaseSetting():
    #使用主题功能， 默认为False
    enable_themes = True
    use_bootswatch =  True

class GlobalSettings():
    #后台名
    site_title = '溪枫教育'
    #底部@
    site_footer = 'python有声'
    #菜单收缩
    menu_style = 'accordion'


class EmailVerifyRecordAdmin():

    list_display = ['code', 'email', 'send_type','send_time']
    search_fields =  ['code', 'email', 'send_type']
    list_filter =  ['code', 'email', 'send_type','send_time']


class BannerAdmin():
    list_display = ['title', 'image', 'url','index','add_time']
    search_fields = ['title', 'image', 'url','index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']




xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)