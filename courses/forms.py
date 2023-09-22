from django import forms
from .models import Course, Category, Levels


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # categories = Category.objects.all()
        # levels = Levels.objects.all()

        # self.fields['category'].choices = categories

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
