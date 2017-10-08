from django import forms
from .models import Deal


class Dealform(forms.ModelForm):
    class Meta:
        model = Deal
        fields =  [
            'title',
            'description',
            'publish_date',
            'expire_date',
            'active',
        ]