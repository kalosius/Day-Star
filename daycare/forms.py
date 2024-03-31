from django import forms
from .models import Sitter, Baby, Payment, Procurement

class SitterForm(forms.ModelForm):
    name = forms.CharField(label="", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Full Name"}), required=True)
    gender = forms.CharField(label="", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Gender"}), required=True)
    location = forms.CharField(label="", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Location"}), required=True)
    # date_of_birth = forms.DateTimeField(label="", widget=forms.DateTimeField(attrs={'class': 'form-control', 'placeholder': 'Date of Birth'}), required=True)
    next_of_kin = forms.CharField(label="", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Next of Kin"}))
    nin = forms.CharField(label="", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"NIN"}), required=True)
    recommender_name = forms.CharField(label="", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Recommender Name"}), required=True)
    religion = forms.CharField(label="", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Religion"}))
    education_level = forms.CharField(label="", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Education Level"}))
    sitter_number = forms.IntegerField(label="", widget=forms.NumberInput(attrs={"class":"form-control", "placeholder":"Sitter Number"}), required=True)
    contact1 = forms.CharField(label="", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Phone 1"}), required=True)
    contact2 = forms.CharField(label="", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Phone 2"}))

    class Meta:
        model = Sitter
        fields = ['name', 'gender', 'location', 'next_of_kin', 'nin', 'recommender_name', 'religion', 'education_level', 'sitter_number', 'contact1', 'contact2']


class BabyForm(forms.ModelForm):
    name = forms.CharField(label="", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Full Name"}), required=True)
    gender = forms.CharField(label="", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Gender"}), required=True)
    # age = forms.IntegerField(label="", widget=forms.IntegerField(attrs={"class":"form-control", "placeholder":"Age"}), required=True)
    location = forms.CharField(label="", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Location"}), required=True)
    brought_by = forms.CharField(label="", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Full Name of Owner"}), required=True)
    parents_names = forms.CharField(label="", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Parent's Name"}), required=True)
    period_of_stay = forms.CharField(label="", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Period Of Stay"}), required=True)
    baby_number = forms.IntegerField(label="", widget=forms.NumberInput(attrs={"class":"form-control", "placeholder":"Baby ID Number"}))
    
    class Meta:
        model = Baby
        fields = '__all__'


class PaymentForm(forms.ModelForm):
    baby =forms.CharField(label="Baby", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Select Baby"}))
    amount = forms.DecimalField(label="Amount", widget=forms.NumberInput(attrs={"class":"form-control", "placeholder":"Ugx"}))
    payment_type = forms.CharField(label="Baby", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Payment Type"}))
    
    class Meta:
        model = Payment
        fields = '__all__'


class ProcurementForm(forms.ModelForm):
    item_name = forms.CharField(label="Item Name", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"E.g Apples"}), required=True)
    quantity = forms.IntegerField(label="Quantity", widget=forms.NumberInput(attrs={"class":"form-control", "placeholder":""}), required=True)
    unit_price = forms.IntegerField(label="Unit Price", widget=forms.NumberInput(attrs={"class":"form-control", "placeholder":""}), required=True)
    
    class Meta:
        model = Procurement
        fields = '__all__'
