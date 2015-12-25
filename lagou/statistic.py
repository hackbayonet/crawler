# -*- coding: utf-8 -*-
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['lagou']


def demand(key):
    demandCompanyCount = {}
    demandjobCount = {}
    for eachData in db.info.find({"classify": key}):
        city = eachData['city']
        demandjobCount[city] = demandjobCount.get(city, 0) + 1  # 统计每个城市招聘的职位
        demandCompanyCount[city] = demandCompanyCount.get(city, set())
        demandCompanyCount[city].add(eachData['companyName'])
    for each in demandCompanyCount:
        demandCompanyCount[each] = len(demandCompanyCount[each])  # 统计每个城市招聘的公司

    sort_list = sorted(demandCompanyCount.iteritems(), key=lambda asd: asd[1], reverse=True)  # 对招聘公司计数的字典排序
    demandCompany = []
    demandjob = []
    city = []

    for each in sort_list:
        city.append(each[0])
        demandCompany.append(each[1])
        demandjob.append(demandjobCount[each[0]])
    db.demand.insert({'demandCompany': demandCompany, 'demandjob': demandjob, 'city': city})






def main():
    demand('python')

if __name__ == '__main__':
    main()
