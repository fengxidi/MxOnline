# _*_ coding: utf-8 _*_
__auther__ = 'guozheng'
__date__ = '2019-10-2 14:15'

import xadmin

from .models import CityDict, CourseOrg, Teacher

class CityDictAdmin():
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']

class CourseOrgAdmin():
    list_display = ['name', 'desc', 'category', 'students','course_nums', 'click_nums', 'fav_nums', 'address', 'city', 'add_time']
    search_fields = ['name', 'desc', 'category', 'students','course_nums', 'click_nums', 'fav_nums', 'address', 'city']
    list_filter = ['name', 'desc', 'category', 'students','course_nums',  'click_nums', 'fav_nums', 'address', 'city', 'add_time']

class TeacherAdmin():
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums', 'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums']
    list_filter = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums', 'add_time']

xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)