from django import forms
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
            'default_eircode': 'Eircode',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'
       # exclude = ('guardian',)
        widgets = {'guardian': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_of_birth'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'dd-mm-yyyy',
                'class': 'form-control'
                }
            )
        self.fields['guardian'].widget = forms.HiddenInput()
