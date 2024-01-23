from django.forms import ModelForm

from accounts.models import Profile


class CustomerProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            'phone_number',
            'address', ...]
