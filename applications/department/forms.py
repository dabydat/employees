from django import forms


class DepartmentForm(forms.Form):
    """Department definition."""

    new_department_name = forms.CharField(max_length=60, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    )
    )
    new_department_acronym = forms.CharField(max_length=60, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    )
    )
    new_employee_name = forms.CharField(max_length=60, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    )
    )
    new_employee_last_name = forms.CharField(max_length=60, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    )
    )
