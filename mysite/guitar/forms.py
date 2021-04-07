from django import forms


class Contact(forms.Form):
    subject = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
