from django import forms

class Form1(forms.Form):
    st_no = forms.CharField(max_length=255)

class Form2(forms.Form):
    st_no = forms.CharField(max_length=255)
