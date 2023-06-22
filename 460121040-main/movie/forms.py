from django import forms
from .models import Car,Rezervation,Testimonial

class CarForm(forms.ModelForm):
    class Meta:
        model=Car
        fields=['Marka','Model','Yil']

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    mesaj = forms.CharField(max_length=50)

class RezervationForm(forms.ModelForm):
    class Meta:
        model=Rezervation
        fields=['full_name','telephone','email','date','description']

class TestimonialForm(forms.ModelForm):
    class Meta:
        model=Testimonial
        fields=['Yorum']