#-*- coding:utf-8 -*-
from django import forms


class SearchForm(forms.Form):
    form_key_word = forms.CharField(required=False,
                                    label=u"项目名称：",
                                    # error_messages={'required': u'请输入关键词'},
                                    widget=forms.forms.TextInput(
                                        attrs={'size': '25',
                                               'class': 'forms',
                                               'placeholder': u"请输入项目名（支持模糊查询）",})
                                    )
    form_pid = forms.CharField(required=False,
                               label=u"批准号：",
                               widget=forms.forms.TextInput(
                                   attrs={'size': '25',
                                          'class': 'forms',
                                          'placeholder': u"批准号（可选）"})
                               )
    form_person = forms.CharField(required=False,
                                  label=u"负责人：",
                                  widget=forms.forms.TextInput(
                                      attrs={'size': '25',
                                             'class': 'forms',
                                             'placeholder': u"项目负责人（可选）"})
                                  )
    form_department = forms.CharField(required=False,

                                      label=u"依托单位：",
                                      widget=forms.forms.TextInput(
                                          attrs={'size': '25',
                                                 'class': 'forms',
                                                 'placeholder': u"项目依托单位（可选）"})
                                      )
    form_classify = forms.CharField(required=False,
                                    label=u"项目类型：",
                                    widget=forms.forms.TextInput(
                                        attrs={'size': '25',
                                               'class': 'forms',
                                               'placeholder': u"项目类型（可选）"}
                                   ))


