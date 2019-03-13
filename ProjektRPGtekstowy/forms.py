from django.forms import ModelForm
import django.forms as forms
from .models import Player

class PlayerForm(forms.Form):
    name = forms.CharField(max_length=255, label= 'Imię Gracza')
    sil = forms.IntegerField(label='Siła', initial=1, min_value=1, max_value=6)
    szc = forms.IntegerField(label='Szczęście', initial=1, min_value=1, max_value=6)
    inte = forms.IntegerField(label='Inteligencja', initial=1, min_value=1, max_value=6)
    zre = forms.IntegerField(label='Zręczność', initial=1, min_value=1, max_value=6)
    hp = forms.IntegerField(label='Punkty Zdrowia', initial=15, widget=forms.NumberInput(attrs={'step':5}), min_value=15, max_value=40)
    points = forms.IntegerField(initial=5, widget=forms.HiddenInput)

    def clean(self):
        x=0
        cleaned_data = super().clean()
        hp = cleaned_data.get("hp")
        sil = cleaned_data.get("sil")
        szc= cleaned_data.get("szc")
        inte = cleaned_data.get("inte")
        zre = cleaned_data.get("zre")
        x=(zre-1)+(inte-1)+(szc-1)+(sil-1)+((hp-15)/5)
        if x>5:
            msg='Dodałeś za dużo punktów przyjacielu :)'
            self.add_error('points',msg)

class AnswersForm(forms.Form):
    end_id=forms.IntegerField(widget=forms.HiddenInput)

class Player2Form(forms.ModelForm):
    points=forms.IntegerField(widget=forms.HiddenInput)
    hp = forms.IntegerField(label='HP',widget=forms.NumberInput(attrs={'step': 5}))
    class Meta():
        model=Player
        fields = '__all__'
        exclude=('name','curent_state','level','hpp',)

        def clean(self):
            cleaned_data = super().clean()
            hp = cleaned_data.get("hp")
            sil = cleaned_data.get("sil")
            szc = cleaned_data.get("szc")
            int = cleaned_data.get("int")
            zre = cleaned_data.get("zre")
            x = (zre - 1) + (int - 1) + (szc - 1) + (sil - 1) + ((hp - 15) / 5)
            point = cleaned_data.get('points')

            if x > point:
                msg = 'Dodałeś za dużo punktów przyjacielu :) '
                self.add_error('sil', msg)