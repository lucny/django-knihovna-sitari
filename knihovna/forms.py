from django import forms
from .models import Kniha


class KnihaForm(forms.ModelForm):
    class Meta:
        model = Kniha
        fields = ['titul', 'autori', 'pocet_stran',
                  'obsah', 'vydavatelstvi', 'rok_vydani',
                  'obalka', 'zanry']