from django.db import models

from wc_line_up_maker.models.formation import Formation
from wc_line_up_maker.models.position import Position


class FormationTemplate(models.Model):
    formation = models.ForeignKey(to=Formation, on_delete=models.RESTRICT, related_name='formation_template', null=False, blank=False)
    position = models.ForeignKey(to=Position, on_delete=models.RESTRICT, related_name='formation_template', null=False, blank=False)

    def __str__(self):
        return f"{self.position}"
