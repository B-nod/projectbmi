from django import forms
from home.models import BmiMeasurement

class BmiForm(forms.ModelForm):
    class Meta:
        model = BmiMeasurement
        fields = "__all__"
        exclude = ("bmi", "message", "user", )

class Subscribe(forms.Form):
    email = forms.EmailField
    subject = forms.CharField()
    message = forms.CharField


    def __str__(self):
        return self.Email