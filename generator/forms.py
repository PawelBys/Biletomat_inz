from datetime import date, timedelta

from django import forms
from django.core.exceptions import ValidationError
from django.forms import DateInput


class BiletForm(forms.Form):
    MONTHS = {
        1: ('styczeń'), 2: ('luty'), 3: ('marzec'), 4: ('kwiecień'),
        5: ('maj'), 6: ('czerwiec'), 7: ('lipiec'), 8: ('sierpień'),
        9: ('wrzesień'), 10: ('październik'), 11: ('listopad'), 12: ('grudzień')
    }
    PLUTONY = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))
    MIESIACE = ( ('styczeń', 'styczeń'), ('luty', 'luty'), ('marzec', 'marzec'), ('kwiecień', 'kwiecień'), ('maj', 'maj'), ('czerwiec', 'czerwiec'), ('lipiec', 'lipiec'), ('sierpień', 'sierpień'), ('wrzesień', 'wrzesień'), ('październik', 'październik'), ('listopad', 'listopad'), ('grudzień', 'grudzień'))
    STOPNIE = ( ('szer. pchor.', 'szer. pchor.'), ('st. szer. pchor.', 'st. szer. pchor.'), ('kpr. pchor.', 'kpr. pchor.'), ('st. kpr. pchor.', 'st. kpr. pchor.'), ('plut. pchor.', 'plut. pchor.'), ('sierż. pchor.', 'sierż. pchor.'))
    TYP = (('przepustkę jednorazową', 'PJ'), ('urlop', 'Urlop'))
    TAM = (('', 'tam'), (' i z powrotem', 'tam i z powrotem'))
    POCIAGI = ("osobowym", "Osobowy"), ("pospiesznym", "TLK"), ("ekspresowym", "IC/EIC/EIP")
    AUTOBUSY = ("zwykłej", "Zwykły"), ("przyspieszonej", "Przyspieszony")


    def clean(self):
        cleaned_data = self.cleaned_data
        end_date = cleaned_data.get('data_przyjazdu')
        start_date = cleaned_data.get('data_wyjazdu')
        if end_date and start_date:
            if end_date < start_date:
                self.add_error('data_przyjazdu', 'Event end date should not occur before start date.')
        return cleaned_data


    typ = forms.CharField(widget=forms.Select(choices=TYP))
    imie_nazwisko = forms.CharField(max_length=50, label="Imię i nazwisko")
    stopien = forms.CharField(widget=forms.Select(choices=STOPNIE), label="Stopień")
    adres = forms.CharField(max_length=100, initial='', help_text="WZÓR: ul. Kolejowa 7/23, 01-476 Warszawa")
    pluton = forms.CharField(widget=forms.Select(choices=PLUTONY))
    data_wyjazdu = forms.DateField(widget=DateInput(), initial=date.today(), help_text="Data z blankietu (np. sobota, nie piątek)")
    data_powrotu = forms.DateField( widget=DateInput(), initial=date.today())
    tam_z_powrotem = forms.CharField(widget=forms.Select(choices=TAM), required=False, label="Tam/Tam i z powrotem", help_text="Czy składasz wniosek z biletem w jedną, czy w obie strony?")
    miasto = forms.CharField(max_length=30, label="Miasto (z biletu)")
    miesiac = forms.CharField(widget=forms.Select(choices=MIESIACE), label="Miesiąc", help_text="Miesiąc za jaki chcesz otrzymać należność")
    typ_pociagu = forms.MultipleChoiceField(choices=POCIAGI, widget=forms.CheckboxSelectMultiple(attrs={'class':'czekbox'}), required=False, label="Typ pociągu")
    typ_autobusu = forms.MultipleChoiceField(choices=AUTOBUSY, widget=forms.CheckboxSelectMultiple(attrs={'class':'czekbox'}), required=False)
    kwota = forms.DecimalField(decimal_places=2, max_digits=10, label="Suma kwot z biletów")


