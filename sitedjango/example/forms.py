from django import forms
from .models import Agnks

class AddDataForms(forms.Form):
    # own = forms.CharField(max_length=255, initial='own')
    date = forms.CharField(max_length=255, label="Дата")
    name = forms.CharField(max_length=255, label="Номер авто")
    waybill = forms.CharField(max_length=255, label="Номер путевого листа")
    amount = forms.FloatField( label="Объем")
    column = forms.CharField(max_length=255, label="Номер колонны")
    note = forms.CharField(max_length=255, label="Филиал")