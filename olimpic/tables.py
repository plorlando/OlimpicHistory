import django_tables2 as tables
from .models import Noc, Athlete_events

class NocTable(tables.Table):
    editar = tables.TemplateColumn('''<a type="button" class="btn-primary btn-sm" href="{% url 'olimpic:noc_update' record.pk %}">Editar</a>''')
    
    class Meta:
        model = Noc
        fields = ('editar', 'noc',  'region', 'notes')
        

class AthletesTable(tables.Table):
    editar = tables.TemplateColumn('''<a type="button" class="btn-primary btn-sm" href="{% url 'olimpic:athlete_update' record.id %}">Editar</a>''')
    
    class Meta:
        model = Athlete_events
        fields = ('editar', 'name',  'team', 'noc', 'games', 'year', 'season', 'city', 'sport', 'event', 'medal')