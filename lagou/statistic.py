# -*- coding: utf-8 -*-
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['lagou']


def demand(key):
    demandCompanyCount = {}
    demandjobCount = {}
    for eachData in db.info.find({"classify": key}):
        city = eachData['city']
        demandjobCount[city] = demandjobCount.get(city, 0) + 1    # 统计每个城市招聘的职位
        demandCompanyCount[city] = demandCompanyCount.get(city, set())
        demandCompanyCount[city].add(eachData['companyName'])
    for each in demandCompanyCount:
        demandCompanyCount[each] = len(demandCompanyCount[each])  # 统计每个城市招聘的公司
    db.demand.insert({'key': key, 'demandCompany': demandCompanyCount, 'demandJob': demandjobCount})


def main():
    demand('python')
    demand('php')
if __name__ == '__main__':
    main()
