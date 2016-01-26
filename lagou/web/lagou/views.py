# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from models import Info, Demand
import json


def home(request):
    return render(request, 'home.html')


def detail(request, keys):
    object = Demand.objects(key=keys)[0]
    demand = {}
    demand['city'] = [e.encode('utf8') for e in object.city[0:10]]
    demand['demandCompany'] = object.demandCompany[0:10]
    demand['demandJob'] = object.demandjob[0:10]
    return render(request, 'chart.html', {'key': keys,
                                          'demand': json.dumps(demand, encoding="UTF-8", ensure_ascii=False)})


def demand_all(request, keys):
    object = Demand.objects(key=keys)[0]
    demand = {}
    demand['city'] = [e.encode('utf8') for e in object.city]
    demandCompany = object.demandCompany
    demandJob = object.demandjob
    demand['max'] = max(demandJob)
    data = []
    for index, value in enumerate(demand['city']):
        data.append({'name': value, 'value': demandJob[index]})
    demand['data'] = data
    demand['top10'] = data[0:10]
    demand['demandJob'] = demandJob
    return render(request, 'demo.html', {'key': keys,
                                         'demand': json.dumps(demand, encoding="UTF-8", ensure_ascii=False)})


def job(request, key):
    if key not in ('python', 'php'):
        return render(request, '404.html')
    else:
        objects = Demand.objects(key=key)[0]
        demandJob = objects.demandJob
        demandCompany = objects.demandCompany
        sortDemandJob = sorted(demandJob.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)  # 按招聘职位数量降序
        city = [each[0] for each in sortDemandJob][0:10]
        jobTop10 = [each[1] for each in sortDemandJob][0:10]
        companyTop10 = [demandCompany[each] for each in city]
        data = {'key': key, 'city': city, 'jobTop10': jobTop10, 'companyTop10': companyTop10}
        return render(request, 'chart01.html',
                      {'data': json.dumps(data, encoding="UTF-8", ensure_ascii=False),
                       })