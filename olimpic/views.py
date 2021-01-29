from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .models import Noc, Athlete_events
from .tables import *
from .filters import *
from .forms import *

def home(request):
    return render(request, 'home.html')


class NOCList(SingleTableMixin, FilterView):
    model = Noc
    table_class = NocTable
    template_name = 'noc_list.html'
    filterset_class = NOCFilter
    paginate_by = 20

    def get_queryset(self):
        return Noc.objects.all().order_by('region')

    def dispatch(self, *args, **kwargs):
        return super(NOCList, self).dispatch(*args, **kwargs)


def NOCUpdate(request, pk):
    template = 'noc_form.html'
    registro = get_object_or_404(Noc, noc=pk)
    print(registro)
    form = NocForm(request.POST or None, instance=registro)
    noc_record = Noc.objects.get(noc=pk)

    if form.is_valid():
        form.save()
        return redirect('olimpic:noc_list')

    return render(request, template, {"form": form, "noc_infos": noc_record})

class NocNewView(CreateView):
    model = Noc
    form_class = NocForm
    success_url = reverse_lazy('olimpic:noc_list')
    template_name = 'noc_new.html'

    def dispatch(self, *args, **kwargs):
        return super(NocNewView, self).dispatch(*args, **kwargs)


class NocDeleteView(DeleteView):
    model = Noc
    success_url = reverse_lazy('olimpic:noc_list')
    template_name = 'noc_delete_confirm.html'

    def dispatch(self, *args, **kwargs):
        return super(NocDeleteView, self).dispatch(*args, **kwargs)



class AthleteList(SingleTableMixin, FilterView):
    model = Athlete_events
    table_class = AthletesTable
    template_name = 'athletes.html'
    filterset_class = AthletesFilter
    paginate_by = 100

    def get_queryset(self):
        return Athlete_events.objects.all().order_by('name')

    def dispatch(self, *args, **kwargs):
        return super(AthleteList, self).dispatch(*args, **kwargs)


def AthleteUpdate(request, pk):
    template = 'athlete_form.html'
    registro = get_object_or_404(Athlete_events, id=pk)
    print(registro)
    form = AthleteForm(request.POST or None, instance=registro)
    athlete_record = Athlete_events.objects.get(id=pk)

    if form.is_valid():
        form.save()
        return redirect('olimpic:athlete_list')

    return render(request, template, {"form": form, "athlete_infos": athlete_record})

class AthleteNewView(CreateView):
    model = Athlete_events
    form_class = AthleteForm
    success_url = reverse_lazy('olimpic:athlete_list')
    template_name = 'athlete_new.html'

    def dispatch(self, *args, **kwargs):
        return super(AthleteNewView, self).dispatch(*args, **kwargs)


class AthleteDeleteView(DeleteView):
    model = Athlete_events
    success_url = reverse_lazy('olimpic:athlete_list')
    template_name = 'athlete_delete_confirm.html'

    def dispatch(self, *args, **kwargs):
        return super(AthleteDeleteView, self).dispatch(*args, **kwargs)