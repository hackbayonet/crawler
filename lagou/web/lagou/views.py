# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from models import Demand
from django.http import HttpResponseRedirect
import json


def home(request):
    return render(request, 'home.html')


def demand_all(request, keys):
    objects = Demand.objects(key=keys)[0]
    demandJob = objects.demandJob
    sortDemandJob = sorted(demandJob.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
    city = [each[0] for each in sortDemandJob]
    jobNumber = [each[1] for each in sortDemandJob]
    mapData = []
    for each in city:
        mapData.append({'name': each, 'value': demandJob[each]})
    dataTop10 = mapData[0:10]
    maxData = jobNumber[0]
    data = {'mapData': mapData, 'city': city, 'jobNumber': jobNumber, 'dataTop10': dataTop10, 'maxData': maxData}
    return render(request, 'demo.html', {'key': keys,
                                         'data': json.dumps(data, encoding="UTF-8", ensure_ascii=False)})


def one(request, key):
    objects = Demand.objects(key=key)[0]
    demandJob = objects.demandJob
    demandCompany = objects.demandCompany
    sortDemandJob = sorted(demandJob.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)  # 按招聘职位数量降序
    city = [each[0] for each in sortDemandJob][0:10]
    jobTop10 = [each[1] for each in sortDemandJob][0:10]
    companyTop10 = [demandCompany[each] for each in city]
    data = {'city': city, 'jobTop10': jobTop10, 'companyTop10': companyTop10}
    return render(request, 'chart01.html',
                  {'key': key,
                   'data': json.dumps(data, encoding="UTF-8", ensure_ascii=False),
                   })


def two(request, keys):
    objects = Demand.objects(key=keys)[0]
    demandJob = objects.demandJob
    sortDemandJob = sorted(demandJob.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
    city = [each[0] for each in sortDemandJob]
    jobNumber = [each[1] for each in sortDemandJob]
    mapData = []
    for each in city:
        mapData.append({'name': each, 'value': demandJob[each]})
    dataTop10 = mapData[0:10]
    maxData = jobNumber[0]
    data = {'mapData': mapData, 'city': city, 'jobNumber': jobNumber, 'dataTop10': dataTop10, 'maxData': maxData}
    return render(request, 'chart02.html', {'key': keys,
                                         'data': json.dumps(data, encoding="UTF-8", ensure_ascii=False)})


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
                elif status == 'two':
                    result = two(request, key)
                    return result
            else:
                return render(request, '404.html')   # 参数中没有status, 返回404
        else:
            return render(request, '404.html')  # 非 get和post访问, 返回404