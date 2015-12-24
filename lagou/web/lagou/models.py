from django.db import models
from mongoengine import *
connect('lagou')


class Info(Document):
    classify = StringField(max_length=25, required=True)
    city = StringField(max_length=25, required=True)
    companyName = StringField(max_length=50, required=True)
    companySize = StringField(max_length=25, required=True)
    createTime = StringField(max_length=50, required=True)
    education = StringField(max_length=25, required=True)
    financeStage = StringField(max_length=25, required=True)
    industryField = StringField(max_length=25, required=True)
    jobNature = StringField(max_length=25, required=True)
    positionId = StringField(max_length=25, required=True)
    positionName = StringField(max_length=50, required=True)
    positionType = StringField(max_length=50, required=True)
    salary = StringField(max_length=25, required=True)
    workYear = StringField(max_length=25, required=True)

