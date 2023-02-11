from django import forms
from django.contrib.auth.models import User
from django.db.models import Q

from wc_line_up_maker.models.formation import Formation
from wc_line_up_maker.models.squad import Squad


class LineUpForm(forms.Form):
    name = forms.CharField(max_length=200, required=True)
    squad = forms.ModelChoiceField(queryset=Squad.objects.all(), required=True)
    formation = forms.ModelChoiceField(queryset=Formation.objects.all(), required=True)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        admin = User.objects.get(id=1)
        current_user = self.request.user
        formation_queryset = Formation.objects.filter(Q(creator=admin) & Q(creator=current_user))
        self.fields['formation'].queryset = formation_queryset

    def clean(self):
        if self.cleaned_data :
            return self.cleaned_data
