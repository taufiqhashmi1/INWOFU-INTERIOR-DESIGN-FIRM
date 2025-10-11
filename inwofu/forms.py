# forms.py
from django import forms
from .models import ContactMessage  # 1. Import your ContactMessage model

# 2. Change inheritance from forms.Form to forms.ModelForm
class ContactForm(forms.ModelForm):
    # 3. Add a class Meta to link the form to the model
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        
        # 4. Move the widgets inside the Meta class
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-yellow-900',
                'placeholder': 'Your Name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-yellow-900',
                'placeholder': 'you@example.com',
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-yellow-900',
                'placeholder': 'Tell us about your project...',
                'rows': 4,
            }),
        }