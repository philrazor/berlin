from django import forms
from .models import Make, CarModel

class SearchForm(forms.Form):
    brand = forms.ModelChoiceField(queryset=Make.objects.all(), empty_label="Select a brand")
    model = forms.ModelChoiceField(queryset=CarModel.objects.all(), empty_label="Select a model", required=False)
    year = forms.ChoiceField(choices=[(year, year) for year in range(2000, 2025)], required=False)