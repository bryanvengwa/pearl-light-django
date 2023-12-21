from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name (required)', max_length=100, required=True)
    phone = forms.CharField(label='Phone (optional)', max_length=20, required=False)
    email = forms.EmailField(label='Email Address (required)', required=True)
    message = forms.CharField(label='Your message*', widget=forms.Textarea, required=True)
