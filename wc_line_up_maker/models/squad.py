from django.db import models

#from wc_line_up_maker.models.player import Player


class Squad(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    country = models.CharField(max_length=200, null=False, blank=False)
    flag = models.CharField(max_length=200, null=True, blank=True)
    #players = models.ManyToManyField(to=Player, related_name='squad')

    def __str__(self):
        return f"{self.name} - {self.country} {self.flag}"
