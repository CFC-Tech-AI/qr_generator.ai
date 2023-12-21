from django import forms
from .models import QRData 

class QRDataForm(forms.ModelForm):
    class Meta:
        model = QRData
        fields = ['data']

