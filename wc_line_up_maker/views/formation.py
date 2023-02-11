from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.forms import inlineformset_factory, ModelChoiceField
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView

from wc_line_up_maker.form.formation import FormationForm, FormationTemplateForm
from wc_line_up_maker.models.formation import Formation
from wc_line_up_maker.models.formation_template import FormationTemplate
from wc_line_up_maker.models.position import Position


class FormationListView(ListView):
    template_name = "formation.html"
    model = Formation

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['admin_user'] = User.objects.get(pk=1)
        return context


class FormationDetailView(DetailView):
    template_name = "formation_detail.html"
    model = Formation


class FormationFormView(LoginRequiredMixin, FormView):
    template_name = "formation_form.html"
    form_class = FormationForm

    def form_valid(self, form):
        creator = self.request.user
        formation = Formation.objects.create(additionnal_info=form.cleaned_data['additionnal_info'],
                                             creator=creator,
                                             defender_number=form.cleaned_data['defender_number'],
                                             midfielder_number=form.cleaned_data['midfielder_number'],
                                             forward_number=form.cleaned_data['forward_number'])

        return HttpResponseRedirect('/formation/template/create/' + str(formation.pk))


@login_required
def create_formation_template(request, pk):
    formation = Formation.objects.get(id=pk)
    def_formation_template = inlineformset_factory(Formation,
                                                   FormationTemplate,
                                                   fields=('position',),
                                                   min_num=formation.defender_number,
                                                   max_num=formation.defender_number,
                                                   validate_min=True,
                                                   can_delete=False)

    mid_formation_template = inlineformset_factory(Formation,
                                                   FormationTemplate,
                                                   fields=('position',),
                                                   min_num=formation.midfielder_number,
                                                   max_num=formation.midfielder_number,
                                                   validate_min=True,
                                                   can_delete=False)

    for_formation_template = inlineformset_factory(Formation,
                                                   FormationTemplate,
                                                   fields=('position',),
                                                   min_num=formation.forward_number,
                                                   max_num=formation.forward_number,
                                                   validate_min=True,
                                                   can_delete=False)

    def_pos_queryset = Position.objects.filter(type='Defender')
    mid_pos_queryset = Position.objects.filter(type='Midfielder')
    for_pos_queryset = Position.objects.filter(type='Forward')
    def_form_queryset = FormationTemplate.objects.filter(position__type='Defender')
    mid_form_queryset = FormationTemplate.objects.filter(position__type='Midfielder')
    for_form_queryset = FormationTemplate.objects.filter(position__type='Forward')

    if request.method == 'POST':
        def_formset = def_formation_template(request.POST, instance=formation, prefix='defenders')
        mid_formset = mid_formation_template(request.POST, instance=formation, prefix='midfielders')
        for_formset = for_formation_template(request.POST, instance=formation, prefix='forwards')
        if def_formset.is_valid() and mid_formset.is_valid() and for_formset.is_valid():
            gk = Position.objects.get(abbreviation='GK')
            if not FormationTemplate.objects.filter(formation=formation, position=gk).exists():
                FormationTemplate.objects.create(formation=formation, position=gk)

            def_formset.save()
            mid_formset.save()
            for_formset.save()
            return HttpResponseRedirect('/')
        else:
            return render(request,
                          'formation_template_form.html',
                          {'def_errors': def_formset.errors,
                           'mid_errors': mid_formset.errors,
                           'for_errors': for_formset.errors,
                           'formation': formation,
                           'def_formset': def_formset,
                           'mid_formset': mid_formset,
                           'for_formset': for_formset})
    else:
        def_formset = def_formation_template(queryset=def_form_queryset, instance=formation, prefix='defenders')
        mid_formset = mid_formation_template(queryset=mid_form_queryset, instance=formation, prefix='midfielders')
        for_formset = for_formation_template(queryset=for_form_queryset, instance=formation, prefix='forwards')
        for form in def_formset:
            form.fields['position'].queryset = def_pos_queryset
        for form in mid_formset:
            form.fields['position'].queryset = mid_pos_queryset
        for form in for_formset:
            form.fields['position'].queryset = for_pos_queryset
        return render(request,
                      'formation_template_form.html',
                      {'formation': formation,
                       'def_formset': def_formset,
                       'mid_formset': mid_formset,
                       'for_formset': for_formset})
