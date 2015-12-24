#-*- coding:utf-8 -*-
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render_to_response
import datetime
from django.http import HttpResponse
from models import Ctr
from django.db.models import Q
from django.template import RequestContext
# from django.shortcuts import render


def my_pagination(request, objects):
    after_range_num = 3
    befor_range_num = 3
    page_size = 15
    paginator = Paginator(objects, page_size)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        page_objects = paginator.page(page)
    except EmptyPage:
        page_objects = paginator.page(paginator.num_pages)
    except (InvalidPage, PageNotAnInteger):
        page_objects = paginator.page(1)
    if page >= after_range_num:
        page_range = paginator.page_range[page-after_range_num:page+befor_range_num]
    else:
        page_range = paginator.page_range[0:int(page)+befor_range_num]
    return page_objects, page_range


def my_view(request):
    if request.method == 'GET':
        now = datetime.datetime.now().strftime("%Y-%m-%d %A")
        global condition
        if 'name' in request.GET or 'id' in request.GET or 'leader' in request.GET or 'sponsor' in request.GET or 'status' in request.GET or 'type' in request.GET:
            if 'page' not in request.GET:
                condition = request.META['QUERY_STRING']
            name = request.GET['name']
            id = request.GET['id']
            leader = request.GET['leader']
            status = request.GET['status']
            sponsor = request.GET['sponsor']
            type = request.GET['type']
            objects = Ctr.objects.filter(Q(Ctr_name__contains='%s' % name) &
                                         Q(Ctr_id__contains='%s' % id) &
                                         Q(Ctr_leader__contains='%s' % leader) &
                                         Q(Ctr_status__contains='%s' % status) &
                                         Q(Ctr_sponsor__contains='%s' % sponsor) &
                                         Q(Ctr_type__contains='%s' % type))
            counts = objects.count()
            search_object, page_range = my_pagination(request, objects)
            return render_to_response('ctr.html', {
                'now': now,
                'objects': search_object,
                'counts': counts,
                'page_range': page_range,
                'condition': condition

            })
        else:
            objects = Ctr.objects.filter().all()
            counts = objects.count()
            search_object, page_range = my_pagination(request, objects)
            return render_to_response('ctr.html', {
                'now': now,
                'objects': search_object,
                'counts': counts,
                'page_range': page_range,

            })


def detail(request):
    now = datetime.datetime.now().strftime("%Y-%m-%d %A")
    if 'regid' in request.GET:
        id = request.GET['regid']
        # try:
        objects = Ctr.objects.filter(Ctr_id='%s' % id)[0]
        return render_to_response('ctr_detail.html', {
            'now': now,
            'objects': objects,
            })
        # except Exception:
        #     return HttpResponse(id)
        # return  HttpResponse(objects.count())
    else:
        return HttpResponse('403')


