from django.db import models

from wc_line_up_maker.models.line_up import LineUp
from wc_line_up_maker.models.player import Player
from wc_line_up_maker.models.position import Position


class LineUpTemplate(models.Model):
    line_up = models.ForeignKey(to=LineUp, on_delete=models.CASCADE, related_name='line_up_template')
    position = models.ForeignKey(to=Position, on_delete=models.CASCADE, related_name='line_up_template')
    player = models.ForeignKey(to=Player, on_delete=models.CASCADE, related_name='line_up_template')

    def __str__(self):
        return f"{self.line_up} : {self.position} - {self.player}"
