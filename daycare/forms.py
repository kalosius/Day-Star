from django import forms
from .models import Sitter, Baby, Payment, Procurement

class SitterForm(forms.ModelForm):
    class Meta:
        model = Sitter
        fields = '__all__'

class BabyForm(forms.ModelForm):
    class Meta:
        model = Baby
        fields = '__all__'

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'

class ProcurementForm(forms.ModelForm):
    class Meta:
        model = Procurement
        fields = '__all__'
