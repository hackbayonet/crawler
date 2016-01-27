# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from models import Demand
from django.http import HttpResponseRedirect
import json


def home(request):
    return render(request, 'home.html')


def one(request, key):
    objects = Demand.objects(key=key)[0]
    demand_job = objects.demandJob
    demand_company = objects.demandCompany
    sort_demand_job = sorted(demand_job.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)  # 按招聘职位数量降序
    city = [each[0] for each in sort_demand_job][0:10]
    job_top10 = [each[1] for each in sort_demand_job][0:10]
    company_top10 = [demand_company[each] for each in city]
    data = {'city': city, 'jobTop10': job_top10, 'companyTop10': company_top10}
    return render(request, 'chart01.html',
                  {'key': key,
                   'data': json.dumps(data, encoding="UTF-8", ensure_ascii=False),
                   })


def two(request, keys):
    objects = Demand.objects(key=keys)[0]
    demand_job = objects.demandJob
    sort_demand_job = sorted(demand_job.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
    city = [each[0] for each in sort_demand_job]
    job_number = [each[1] for each in sort_demand_job]
    map_data = []
    for each in city:
        map_data.append({'name': each, 'value': demand_job[each]})
    data_top10 = map_data[0:10]
    max_data = job_number[0]
    data = {'mapData': map_data, 'city': city, 'jobNumber': job_number, 'dataTop10': data_top10, 'maxData': max_data}
    return render(request, 'chart02.html', {'key': keys,
                                            'data': json.dumps(data, encoding="UTF-8", ensure_ascii=False)})


def three(request, key):
    objects = Demand.objects(key=key)[0]
    work_year = objects.workYear
    work_year_list = []
    for each in work_year:
        work_year_list.append({'name': each, 'value': work_year[each]})
    position = objects.position
    position_list = []
    for each in position:
        position_list.append({'name': each, 'value': position[each]})
    education = objects.education
    education_list = []
    for each in education:
        education_list.append({'name': each, 'value': education[each]})
    company_stage = objects.companyStage
    company_stage_list = []
    for each in company_stage:
        company_stage_list.append({'name': each, 'value': company_stage[each]})
    render_data = {'work_year': work_year_list,
                   'position': position_list,
                   'education': education_list,
                   'company_stage': company_stage_list}

    return render(request, 'chart03.html', {'key': key,
                                            'data': json.dumps(render_data, encoding="UTF-8", ensure_ascii=False)})


def job(request, key):
    if key not in ('python', 'php'):
        return render(request, '404.html')  # job 不存在 返回404
    else:
        if request.method == 'GET':  # get访问, 首次访问
            result = one(request, key)
            return result
        elif request.method == 'POST':  # post 访问, 非首次
            if 'status' in request.POST:
                status = request.POST['status']
                if status == 'home':  # 访问首页
                    return HttpResponseRedirect('/')
                elif status == 'one':
                    result = one(request, key)
                    return result
                elif status == 'two':
                    result = two(request, key)
                    return result
                elif status == 'three':
                    result = three(request, key)
                    return result
                else:
                    return render(request, '404.html')  # status 不存在, 返回404
            else:
                return render(request, '404.html')   # 参数中没有status, 返回404
        else:
            return render(request, '404.html')  # 非 get和post访问, 返回404