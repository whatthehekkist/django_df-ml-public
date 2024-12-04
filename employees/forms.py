from django import forms
from .models import Employee


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'age', 'mobile', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'readonly': 'readonly'}),
        }


class DeleteForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'age', 'mobile', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'readonly': 'readonly'}),
            'age': forms.TextInput(attrs={'readonly': 'readonly'}),
            'mobile': forms.TextInput(attrs={'readonly': 'readonly'}),
            'address': forms.TextInput(attrs={'readonly': 'readonly'}),
        }


class InsertForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'age', 'mobile', 'address']