from django import forms

class URLForm(forms.Form):
    url = forms.CharField(label='Enter a URL', max_length=500)