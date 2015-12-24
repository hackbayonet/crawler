# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class LagouItem(Item):
    city = Field()
    companyName = Field()
    companySize = Field()
    createTime = Field()
    education = Field()
    financeStage = Field()
    industryField = Field()
    jobNature = Field()
    positionId = Field()
    positionName = Field()
    positionType = Field()
    salary = Field()
    workYear = Field()
    classify = Field()
    pass
