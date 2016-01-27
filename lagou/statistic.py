# -*- coding: utf-8 -*-
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['lagou']


def demand(key):
    # chart01 chart02
    demand_company_count = {}
    demand_job_count = {}
    for eachData in db.info.find({"classify": key}):
        city = eachData['city']
        demand_job_count[city] = demand_job_count.get(city, 0) + 1    # 统计每个城市招聘的职位
        demand_company_count[city] = demand_company_count.get(city, set())
        demand_company_count[city].add(eachData['companyName'])
    for each in demand_company_count:
        demand_company_count[each] = len(demand_company_count[each])  # 统计每个城市招聘的公司

    #  chart03
    company_stage = {}
    education = {}
    work_year = {}
    industry = {}
    position = {}
    for each in db.info.find({"classify": key}):
        company_stage[each['financeStage']] = company_stage.get(each['financeStage'], 0) + 1
        education[each['education']] = education.get(each['education'], 0) + 1
        work_year[each['workYear']] = work_year.get(each['workYear'], 0) + 1
        industry[each['industryField']] = industry.get(each['industryField'], 0) + 1
        position[each['positionType']] = position.get(each['positionType'], 0) + 1
    db.demand.insert({'key': key,
                      'demandCompany': demand_company_count,
                      'demandJob': demand_job_count,
                      'companyStage': company_stage,
                      'education': education,
                      'workYear': work_year,
                      'industry': industry,
                      'position': position
                      })


def main():
    demand('python')
    demand('php')
if __name__ == '__main__':
    main()
