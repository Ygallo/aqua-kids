from django import forms
from .models import Course, Category, Levels


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['start_date'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'text', 'placeholder': 'dd-mm-yyyy',
                'class': 'form-control',
                'onfocus': "(this.type='date')",
                }
            )
        self.fields['end_date'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'text', 'placeholder': 'dd-mm-yyyy',
                'class': 'form-control',
                'onfocus': "(this.type='date')",
                }
            )

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
