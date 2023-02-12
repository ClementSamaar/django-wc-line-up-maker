from django.contrib.auth.models import User
from django.db import models


class Formation(models.Model):
    additionnal_info = models.CharField(max_length=200, null=True, blank=True)
    creator = models.ForeignKey(to=User, on_delete=models.RESTRICT, null=False, blank=False, related_name='formation')
    forward_number = models.IntegerField(null=False, blank=True, default=0)
    midfielder_number = models.IntegerField(null=False, blank=True, default=0)
    defender_number = models.IntegerField(null=False, blank=True, default=0)

    def __str__(self):
        str = f"{self.defender_number}-{self.midfielder_number}-{self.forward_number} "
        if self.additionnal_info is not None:
            str = str + f"{self.additionnal_info}"

        return str
