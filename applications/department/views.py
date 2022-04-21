from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Department
from applications.employee.models import Employee
from .forms import DepartmentForm
from django.views.generic import FormView, ListView

# Create your views here.


class DepartmentListView(ListView):
    model = Department
    template_name = "department/departments_list.html"
    context_object_name = 'departments'


class NewDepartmentCreateView(FormView):
    template_name = "department/new_department.html"
    form_class = DepartmentForm
    success_url = reverse_lazy("department_app:departments_list")

    def form_valid(self, form):
        new_department = Department(
            name=form.cleaned_data['new_department_name'],
            short_name=form.cleaned_data['new_department_acronym']
        )
        new_department.save()

        name = form.cleaned_data['new_employee_name']
        last_name = form.cleaned_data['new_employee_last_name']
        Employee.objects.create(
            name=name,
            last_name=last_name,
            job_name='1',
            department=new_department
        )

        return super(NewDepartmentCreateView, self).form_valid(form)
