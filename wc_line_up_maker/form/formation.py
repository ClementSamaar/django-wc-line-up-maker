from django import forms
from django.forms import formset_factory

from wc_line_up_maker.models.formation import Formation
from wc_line_up_maker.models.position import Position


class FormationForm(forms.Form):
    additionnal_info = forms.CharField(max_length=200, required=False)
    defender_number = forms.IntegerField(min_value=1, max_value=7)
    midfielder_number = forms.IntegerField(min_value=1, max_value=7)
    forward_number = forms.IntegerField(min_value=1, max_value=7)

    def clean(self):
        if self.cleaned_data['defender_number'] + \
                self.cleaned_data['midfielder_number'] + \
                self.cleaned_data['forward_number'] != 10:
            self.add_error('defender_number', 'You must have a total of 10 position in a formation')
        return self.cleaned_data


class FormationTemplateForm(forms.Form):
    formation = forms.ModelChoiceField(queryset=Formation.objects.all())
    position = forms.ModelChoiceField(queryset=Position.objects.all())
