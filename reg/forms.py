from django import forms
from .models import Student, Subject


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['id_no', 'last_name', 'first_name',
                  'middle_name', 'gender', 'address', 'birth_date']
        widgets = {
            'id_no': forms.TextInput
            (attrs={'class': 'form-control', 'placeholder': 'id number'}),
            'last_name': forms.TextInput
            (attrs={'class': 'form-control', 'placeholder': 'Last name'}),
            'first_name': forms.TextInput
            (attrs={'class': 'form-control', 'placeholder': 'First name'}),
            'birth_date': forms.DateInput
            (attrs={'class': 'form-control', 'type': 'date'}),
        }
