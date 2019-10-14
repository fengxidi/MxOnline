#_*_ coding:utf-8 _*_
from django.shortcuts import render
from django.views.generic import View

from django.shortcuts import render_to_response
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .models import CourseOrg, CityDict

# Create your views here.

class OrgView(View):
    '''
    课程机构列表功能
    '''
    def get(self, request):
        #课程机构
        all_orgs = CourseOrg.objects.all()
        #城市
        all_citys = CityDict.objects.all()
        #热门机构, order_by 排序
        hot_orgs = all_orgs.order_by('-click_nums')[:5]

        #学习人数排名
        sort_orgs = request.GET.get('sort', '')
        if sort_orgs:
            if sort_orgs == 'students':
                all_orgs = all_orgs.order_by('-students')
            elif sort_orgs == 'course_nums':
                all_orgs = all_orgs.order_by('-course_nums')



        #取出筛选城市
        city_id = request.GET.get('city', '')
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        #机构类别筛选
        category  = request.GET.get('ct', '')
        if category:
            all_orgs = all_orgs.filter(category=category)


        org_num = all_orgs.count()
        # 对课程机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_orgs, 5, request=request)
        orgs = p.page(page)

        return render(request, 'org-list.html', {
            'all_orgs': orgs,
            'all_citys': all_citys,
            'org_num': org_num,
            "city_id": city_id,
            "category":category,
            "hot_orgs":hot_orgs,
            "sort_orgs":sort_orgs,
                                }
                      )







