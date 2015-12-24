from django.db import models


class Ctr(models.Model):
    Ctr_name = models.CharField(max_length=255)
    Ctr_id = models.CharField(max_length=20)
    Ctr_stitle = models.CharField(max_length=255)
    Ctr_applicant = models.CharField(max_length=50)
    Ctr_leader = models.CharField(max_length=50)
    Ctr_status = models.CharField(max_length=20)
    Ctr_sponsor = models.CharField(max_length=100)
    Ctr_type = models.CharField(max_length=20)
    Ctr_html = models.TextField()

    def _unicode_(self):
        return (self.Ctr_name,
                self.Ctr_id,
                self.Ctr_stitle,
                self.Ctr_applicant,
                self.Ctr_leader,
                self.Ctr_status,
                self.Ctr_sponsor,
                self.Ctr_type,
                self.Ctr_html
                )
