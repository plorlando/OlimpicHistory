from olimpic.models import Noc
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class NocForm(forms.ModelForm):
    class Meta:
        model = Noc
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(NocForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Salvar'))



