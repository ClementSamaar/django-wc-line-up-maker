from django.db import models
from wc_line_up_maker.models.squad import Squad


class Player(models.Model):
    fname = models.CharField(max_length=200, null=False, blank=False)
    lname = models.CharField(max_length=200, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    shirt_number = models.IntegerField(null=False, blank=False)
    squad = models.ForeignKey(to=Squad, on_delete=models.RESTRICT, related_name='player')

    def __str__(self):
        return f"{self.fname} {self.lname} #{self.shirt_number}"
