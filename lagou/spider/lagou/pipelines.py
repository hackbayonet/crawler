# -*- coding: utf-8 -*-
import pymongo
import logging
from scrapy.conf import settings
from scrapy.exceptions import DropItem
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class LagouPipeline(object):
    def __init__(self):
        self.server = settings['MONGODB_SERVER']
        self.port = settings['MONGODB_PORT']
        self.db = settings['MONGODB_DB']
        self.col = settings['MONGODB_COLLECTION']
        client = pymongo.MongoClient(self.server, self.port)
        db = client[self.db]
        self.collection = db[self.col]

    def process_item(self, item, spider):
        err_msg = ''
        for field, data in item.items():
            if not data:
                err_msg += 'Missing %s of poem from %s\n' % (field, item['positionId'])
        if err_msg:
            raise DropItem(err_msg)
        self.collection.insert(dict(item))
        logging.log(logging.DEBUG,'Item written to MongoDB database %s/%s' % (self.db, self.col))

        # return item

