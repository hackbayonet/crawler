# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from models import Info, Demand


def home(request):
    return render(request, 'home.html')


def detail(request, key):
    object = Demand.objects[0]
    demand = {}
    demand['city'] = object.city[0:10]
    demand['demandCompany'] = object.demandCompany[0:10]
    demand['demandJob'] = object.demandjob[0:10]
    # return HttpResponse(demand)
    # return render(request, 'home.html', {'objects': demand})
    return render(request, 'chart.html', {'demand': demand})
