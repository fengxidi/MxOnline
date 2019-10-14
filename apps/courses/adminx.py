# _*_ coding: utf-8 _*_
__auther__ = 'guozheng'
__date__ = '2019-10-2 11:00'

import xadmin

from .models import Course, Lesson, Video, CourseResourse

class CourseAdmin():
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students','fav_nums','image','click_num','add_time']
    search_fields = ['name', 'desc', 'detail', 'degree',  'students','fav_nums','click_num']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students','fav_nums','click_num','add_time']

class LessonAdmin():
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    #外键course 的name 用双下划线
    list_filter = ['course__name', 'name', 'add_time']

class VideoAdmin():
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']

class CourseResourseAdmin():
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResourse, CourseResourseAdmin)