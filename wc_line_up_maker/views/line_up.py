import itertools

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, FormView

from wc_line_up_maker.form.line_up import LineUpForm
from wc_line_up_maker.models.formation_template import FormationTemplate
from wc_line_up_maker.models.line_up import LineUp
from wc_line_up_maker.models.line_up_template import LineUpTemplate
from wc_line_up_maker.models.player import Player
from wc_line_up_maker.models.position import Position


# class LineUpListView(LoginRequiredMixin, ListView):
#     template_name = "line_up.html"
#     model = LineUp
#
#
# class LineUpDetailView(LoginRequiredMixin, DetailView):
#     template_name = "line_up_detail.html"
#     model = LineUp


def line_up_list_view(request):
    return render(request, 'line_up.html', {'line_up_list': LineUp.objects.all()})


def line_up_detail_view(request, pk):
    line_up = LineUp.objects.get(id=pk)
    line_up_template = LineUpTemplate.objects.filter(line_up=line_up)
    return render(request, 'line_up_detail.html', {'line_up': line_up, 'line_up_template': line_up_template})


class LineUpFormView(LoginRequiredMixin, FormView):
    form_class = LineUpForm
    template_name = 'line_up_form.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        creator = self.request.user
        line_up = LineUp.objects.create(name=form.cleaned_data['name'],
                                        creator=creator,
                                        squad=form.cleaned_data['squad'],
                                        formation=form.cleaned_data['formation'])

        return HttpResponseRedirect(reverse('line_up_template_form', args=[str(line_up.pk)]))


@login_required
def create_line_up_template(request, pk):
    line_up = LineUp.objects.get(id=pk)
    positions = Position.objects.filter(formation_template__formation__line_up=line_up)
    players = Player.objects.filter(squad__line_up=line_up)
    str_positions = [position.name for position in positions]
    formation_template = [formation_template_row for formation_template_row in
                          FormationTemplate.objects.filter(formation=line_up.formation)]

    pos = FormationTemplate.objects.filter(formation=line_up.formation)
    def_pos = FormationTemplate.objects.filter(formation=line_up.formation, position__type='Defender')
    mid_pos = FormationTemplate.objects.filter(formation=line_up.formation, position__type='Midfielder')
    for_pos = FormationTemplate.objects.filter(formation=line_up.formation, position__type='Forward')

    line_up_template = inlineformset_factory(LineUp,
                                             LineUpTemplate,
                                             fields=('position', 'player'),
                                             min_num=11,
                                             max_num=11,
                                             validate_min=True,
                                             can_delete=False)

    formset = line_up_template(queryset=LineUpTemplate.objects.all(), instance=line_up)

    cpt = 0
    for form in formset:
        form.fields['player'].queryset = players
        form.fields['position'].initial = positions[cpt]
        cpt += 1

    if request.method == 'POST':
        post_formset = line_up_template(request.POST, instance=line_up)
        if post_formset.is_valid():
            post_formset.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request,
                          'line_up_template_form.html',
                          {'errors': formset.errors,
                           'line_up': line_up,
                           'position': str_positions,
                           'formset': formset})
    else:
        return render(request,
                      'line_up_template_form.html',
                      {'line_up': line_up,
                       'position': str_positions,
                       'formset': formset})


# form_players = [print(form.data) for form in post_formset]
# for player_i in form_players:
#     for player_j in form_players:
#         if player_i == player_j:
#             sp_err = 'You assigned the same player twice'
#             return render(request,
#                           'line_up_template_form.html',
#                           {'errors': formset.errors,
#                            'sp_err': sp_err,
#                            'line_up': line_up,
#                            'position': str_positions,
#                            'formset': formset})