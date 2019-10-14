# _*_ coding: utf-8 _*_
__auther__ = 'guozheng'
__date__ = '2019-10-2 14:25'
import xadmin

from .models import UserAsk, CourseComment, UserFavorite, UserMessage, UserCourse


class UserAskAdmin():
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    search_fields = ['name', 'mobile', 'course_name']
    list_filter = ['name', 'mobile', 'course_name', 'add_time']


class CourseCommentAdmin():
    list_display = ['user', 'course', 'conments', 'add_time']
    search_fields = ['user', 'course', 'conments']
    list_filter = ['user', 'course', 'conments', 'add_time']


class UserFavoriteAdmin():
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']


class UserMessageAdmin():
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']


class UserCourseAdmin():
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'add_time']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComment, CourseCommentAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
