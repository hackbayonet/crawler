#-*- coding:utf-8 -*-
from django.core.paginator import Paginator, InvalidPage, EmptyPage
import datetime
from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import Project, Detail
from django.template import RequestContext
from forms import SearchForm


def default_condition():
    condition = {'key_word': '',
                 'pid': '',
                 'person': '',
                 'department': '',
                 'classify': '',
                 }
    return condition


def search_condition(form):
    if form.is_valid():
        cd = form.cleaned_data
        condition = {'key_word': cd['form_key_word'],
                     'pid': cd['form_pid'],
                     'person': cd['form_person'],
                     'department': cd['form_department'],
                     'classify': cd['form_classify'],
                     }
    else:
        condition = default_condition()
    return condition


def search_objects(condition):
    objects = Project.objects.filter(Project_name__contains='%s' % condition.get('key_word', ''))
    if condition.get('pid'):
        objects = objects.filter(Project_pid__contains='%s' % condition.get('pid', ''))
    if condition.get('person'):
        objects = objects.filter(Project_person__contains='%s' % condition.get('person'))
    if condition.get('department'):
        objects = objects.filter(Project_department__contains='%s' % condition.get('department', ''))
    if condition.get('classify'):
        objects = objects.filter(Project_classify__contains='%s' % condition.get('classify', ''))
    counts = objects.count()

    return objects, counts


def my_pagination(request, objects):
    after_range_num = 3
    befor_range_num = 3
    page_size = 7
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
    now = datetime.datetime.now().strftime("%Y-%m-%d %A")
    if request.method == 'GET':
        global search_url
        if 'page' not in request.GET:
            search_url = request.META['QUERY_STRING'] #获取url?后的get内容
        form = SearchForm(request.GET)
        condition = search_condition(form)
        objects, counts = search_objects(condition)
        search_object, page_range = my_pagination(request, objects)
        return render_to_response('project_index.html',
                                  {'objects':  search_object,
                                   'page_range': page_range,
                                   'form': form,
                                   'search': search_url,
                                   'condition': condition,
                                   'counts': counts,
                                   'now': now}, context_instance=RequestContext(request))

    else:
        condition = default_condition()
        objects, counts = search_objects(condition)
        search_object, page_range = my_pagination(request, objects)
        form = SearchForm()
        search_url = ''
        return render_to_response('project_index.html',
                                  {'objects': search_object,
                                   'search': search_url,
                                   'page_range': page_range,
                                   'form': form,
                                   'counts': counts,
                                   'now': now}, context_instance=RequestContext(request))


def detail(request):
    now = datetime.datetime.now().strftime("%Y-%m-%d %A")
    if 'pid' in request.GET:
        pid = request.GET['pid']
        try:
            objects = Detail.objects.get(Detail_pid="%s" % pid)
            return render_to_response('detail.html',
                                      {'object': objects,
                                       'now': now
                                       })
        except Exception:
            return HttpResponse('404')
    else:
        return HttpResponse('403')
