from django.forms import ModelForm
from django import forms
from .models import *

class FormPenangkaran(ModelForm):
    class Meta:
        model = Penangkaran
        fields = '__all__'

        widgets = {
            'nama_tempat'    : forms.TextInput({'class':'form-control', 'placeholder':'Nama Tempat', 'required':'required'}),
            'grs_lintang' : forms.NumberInput({'class':'form-control', 'placeholder':'Garis Lintang', 'required':'required', 'step' : '0.0000000001', 'type' : 'number',}),
            'grs_bujur'  : forms.NumberInput({'class':'form-control', 'placeholder':'Garis Bujur', 'required':'required', 'step' : '0.0000000001', 'type' : 'number',}),
        }


class FormPenyu(ModelForm):
    class Meta:
        model = Data
        fields = '__all__'

        widgets = {
            'jenis'  : forms.TextInput({'class':'form-control', 'placeholder':'Jenis Penyu', 'required':'required'}),
            'deskripsi'   : forms.TextInput({'class':'form-control', 'placeholder':'...', 'required':'required'}),
            'gambar'   : forms.FileInput({'class':'form-control', 'required':'required'}),

        }