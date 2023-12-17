from django import forms
from .models import Wish

class WishForm(forms.ModelForm):
    class Meta:
        model = Wish
        fields = ['sender_name', 'title', 'receiver', 'message', 'password', 'signature']

class WishSearchForm(forms.Form):
    wish_id = forms.IntegerField(label='', min_value=1, widget=forms.NumberInput(attrs={'placeholder': 'Enter Wish ID'}))