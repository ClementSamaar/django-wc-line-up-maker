from django.contrib.auth.models import User
from django.db import models

from wc_line_up_maker.models.formation import Formation
from wc_line_up_maker.models.squad import Squad


class LineUp(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    creator = models.ForeignKey(to=User, on_delete=models.RESTRICT, null=False, blank=False, related_name='line_up')
    squad = models.ForeignKey(to=Squad, on_delete=models.RESTRICT, null=False, blank=False, related_name='line_up')
    formation = models.ForeignKey(to=Formation,
                                  on_delete=models.RESTRICT,
                                  null=False,
                                  blank=False,
                                  related_name='line_up')

    def __str__(self):
        return f"{self.name} ({self.squad} - {self.formation})"
