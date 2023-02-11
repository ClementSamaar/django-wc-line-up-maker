from django.views.generic import ListView, DetailView
from wc_line_up_maker.models.squad import Squad


class SquadListView(ListView):
    template_name = "squad.html"
    model = Squad


class SquadDetailView(DetailView):
    template_name = "squad_detail.html"
    model = Squad
