from django.contrib import admin

from wc_line_up_maker.models.formation import Formation
from wc_line_up_maker.models.formation_template import FormationTemplate
from wc_line_up_maker.models.line_up import LineUp
from wc_line_up_maker.models.line_up_template import LineUpTemplate
from wc_line_up_maker.models.player import Player
from wc_line_up_maker.models.position import Position
from wc_line_up_maker.models.squad import Squad

admin.site.register(Squad)
admin.site.register(Player)
admin.site.register(Position)
admin.site.register(Formation)
admin.site.register(FormationTemplate)
admin.site.register(LineUp)
admin.site.register(LineUpTemplate)
