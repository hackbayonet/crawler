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
    key = request.GET['k']
    if key != 'python':
        return render(request, '404.html')
    else:
        return render(request, 'index.html',
                      {'key': key,
                       })