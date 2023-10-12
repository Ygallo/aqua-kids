from django import forms
from datetime import datetime, timedelta
from .models import UserProfile, Student


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postcode',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'
        widgets = {'guardian': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        today = datetime.now()
        min_birthday = today - timedelta(days=14*365)  # Less 14 years old
        max_birthday = today - timedelta(days=3*365)  # Over 3 years old

        self.fields['date_of_birth'] = forms.DateField(
            widget=forms.widgets.DateInput(
                attrs={
                    'type': 'text', 'placeholder': 'dd-mm-yyyy',
                    'class': 'form-control',
                    'onfocus': "(this.type='date')",
                    'max': max_birthday.strftime('%Y-%m-%d'),
                    'min': min_birthday.strftime('%Y-%m-%d'),
                    }
                )
            )
        self.fields['guardian'].widget = forms.HiddenInput()
