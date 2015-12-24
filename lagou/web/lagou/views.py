from django.shortcuts import render
from django.http import HttpResponse
from models import Info


def home(request):
    info = Info.objects()
    return HttpResponse(repr(info))