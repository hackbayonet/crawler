from django.db import models


class Project(models.Model):
    Project_pid = models.CharField(max_length=20)
    Project_name = models.CharField(max_length=100)
    Project_classify = models.CharField(max_length=50)
    Project_person = models.CharField(max_length=50)
    Project_department = models.CharField(max_length=50)
    Project_money = models.CharField(max_length=30)
    Project_time = models.CharField(max_length=50)

    def _unicode_(self):
        return (self.Project_pid,
                self.Project_name,
                self.Project_classify,
                self.Project_person,
                self.Project_department,
                self.Project_money,
                self.Project_time,
                )


class Detail(models.Model):
    Detail_pid = models.CharField(max_length=20, primary_key=True)
    Detail_name = models.CharField(max_length=100)
    Detail_classify = models.CharField(max_length=50)
    Detail_apply = models.CharField(max_length=20)
    Detail_person = models.CharField(max_length=50)
    Detail_job = models.CharField(max_length=50)
    Detail_department = models.CharField(max_length=50)
    Detail_time = models.CharField(max_length=50)
    Detail_money = models.CharField(max_length=50)
    Detail_abstract_chinese = models.CharField(max_length=2000, null=True)
    Detail_keyword_chinese = models.CharField(max_length=500, null=True)
    Detail_abstract_english = models.CharField(max_length=5000, null=True)
    Detail_keyword_english = models.CharField(max_length=500, null=True)
    Detail_abstract_end = models.CharField(max_length=5000, null=True)
    Detail_achievement = models.TextField(null=True)

    def _unicode_(self):
        return (self.Detail_pid,
                self.Detail_name,
                self.Detail_classify,
                self.Detail_person,
                self.Detail_department,
                self.Detail_money,
                self.Detail_time,
                self.Detail_job,
                self.Detail_abstract_chinese,
                self.Detail_keyword_chinese,
                self.Detail_keyword_english,
                self.Detail_abstract_end,
                self.Detail_achievement,
                )



# Create your models here.
