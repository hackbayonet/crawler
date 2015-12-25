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

    def __unicode__(self):
        return (self.city,
                self.classify,
                self.companyName,
                self.companySize,
                self.createTime,
                self.education,
                self.financeStage,
                self.industryField,
                self.jobNature,
                self.positionId,
                self.positionName,
                self.positionType,
                self.salary,
                self.workYear,
                )


class Demand(Document):
    city = ListField()
    demandCompany = ListField()
    demandjob = ListField()

    def __unicode__(self):
        return (self.demandjob,
                self.demandCompany)


