from django import forms
from store.models import Customer


class ProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['birth_date'].widget = forms.DateInput(
            attrs={
                'type': 'date',
                'placeholder': 'dd-mm-yyyy',
                'class': 'form-control'
            }
        )

    class Meta:
        model = Customer
        # fields = ["first_name", "last_name", 'address', 'mobile_number', 'gender', 'birth_date', 'avatar']
        fields = "__all__"
        exclude = ['email']

        labels = {
            'first_name': 'Meno',
            'last_name': 'Priezvisko',
            'birth_date': 'Datum narodenia',
            # 'address': 'Adresa',
            'mobile_number': 'Mobilné číslo',
        }

        help_texts = {
            'mobile_number': 'Zadejte telefonné číslo vo formáte +421',
        }

        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'JohnDoe@example.com'}),
        }