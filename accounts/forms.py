from django import forms
from store.models import Customer


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        # fields = ["first_name", "last_name", 'address', 'mobile_number', 'gender', 'birth_date', 'avatar']
        fields = "__all__"
