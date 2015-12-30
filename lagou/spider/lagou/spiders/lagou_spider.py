# -*- coding: utf-8 -*-
from scrapy.http import FormRequest
from scrapy import Spider
from lagou.items import LagouItem
import json


class LaogouSpider(Spider):
    name = "lagou"
    allowed_domains = ["http://www.lagou.com"]
    form = {
        # 'city': u'成都',
        'pn': '1',
        'kd': 'php',
    }

    def start_requests(self):
        for page in xrange(1, 335):
            self.form['pn'] = repr(page)
            yield FormRequest("http://www.lagou.com/jobs/positionAjax.json",
                              formdata=self.form,
                              callback=self.parse,)
            # break

    def parse(self, response):
        body = json.loads(response.body)
        content = body['content']
        result = content['result']
        item = LagouItem()
        for each in result:
            item['companyName'] = each['companyName']
            item['city'] = each['city']
            item['companySize'] = each['companySize']
            item['createTime'] = each['createTime']
            item['education'] = each['education']
            item['financeStage'] = each['financeStage']
            item['industryField'] = each['industryField']
            item['jobNature'] = each['jobNature']
            item['positionId'] = each['positionId']
            item['positionName'] = each['positionName']
            item['positionType'] = each['positionType']
            item['salary'] = each['salary']
            item['workYear'] = each['workYear']
            item['classify'] = 'php'
            yield item
