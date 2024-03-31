from django import forms
from .models import Votacao


class LoginForm(forms.ModelForm):
  class Meta:
    model = Votacao
    fields = ['cpf']
    
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field_name,field in self.fields.items():
      field.widget.attrs['class'] = 'form-control'
    
    
class VotacaoForm(forms.ModelForm):
  class Meta:
    model = Votacao
    fields = ['voto']