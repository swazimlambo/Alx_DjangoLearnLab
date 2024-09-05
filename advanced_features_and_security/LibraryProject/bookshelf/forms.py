from django.forms import forms

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    published_date = forms.DateField(widget=forms.SelectDateWidget)