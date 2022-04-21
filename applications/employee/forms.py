from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    """Form definition for Employee."""

    class Meta:
        """Meta definition for Employeeform."""

        model = Employee
        fields = ('__all__')
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "age": forms.NumberInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "id_number": forms.NumberInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "job_name": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "image": forms.FileInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "department": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),
            "skills": forms.CheckboxSelectMultiple(),
        }
