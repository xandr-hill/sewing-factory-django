from django import forms
from .models import FabricRoll, Cutting, Sewing, Ironing, Contact

class FabricRollForm(forms.ModelForm):
    class Meta:
        model = FabricRoll
        fields = '__all__'

class CuttingForm(forms.ModelForm):
    class Meta:
        model = Cutting
        fields = '__all__'

class SewingForm(forms.ModelForm):
    class Meta:
        model = Sewing
        fields = '__all__'

class IroningForm(forms.ModelForm):
    class Meta:
        model = Ironing
        fields = '__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
