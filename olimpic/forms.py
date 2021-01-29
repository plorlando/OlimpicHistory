from olimpic.models import Athlete_events, Noc
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class NocForm(forms.ModelForm):
    class Meta:
        model = Noc
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(NocForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Salvar'))


class AthleteForm(forms.ModelForm):
    class Meta:
        model = Athlete_events
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AthleteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Salvar'))
        
        self.helper.layout = Layout(
            Row(
                Column('id_athlete', css_class='form-group col-md-2 mb=0'),
                Column('name', css_class='form-group col-md-2 mb=0'),
                Column('sex', css_class='form-group col-md-2 mb=0'),
                Column('age', css_class='form-group col-md-2 mb=0'),
                css_class='form-row'
            ),
            Row(
                Column('height', css_class='form-group col-md-3 mb=0'),
                Column('weight', css_class='form-group col-md-3 mb=0'),
                Column('team', css_class='form-group col-md-3 mb=0'),
                Column('noc', css_class='form-group col-md-3mb=0'),
                css_class='form-row'
            ),
            Row(
                Column('games', css_class='form-group col-md-3 mb=0'),
                Column('year', css_class='form-group col-md-3 mb=0'),
                Column('season', css_class='form-group col-md-3 mb=0'),
                Column('city', css_class='form-group col-md-3 mb=0'),
                css_class='form-row'
            ),
            Row(
                Column('sport', css_class='form-group col-md-4 mb=0'),
                Column('event', css_class='form-group col-md-4 mb=0'),
                Column('medal', css_class='form-group col-md-4 mb=0'),
                css_class='form-row'
            ),
        )
