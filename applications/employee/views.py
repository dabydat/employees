from venv import create
from .forms import EmployeeForm
from .models import Employee

from django.urls import reverse_lazy

from django.views.generic import (TemplateView,
                                  ListView,
                                  DetailView,
                                  UpdateView,
                                  DeleteView,
                                  CreateView
                                  )

# Create your views here.


class IndexTemplateView(TemplateView):
    template_name = "index.html"


class EmployeeListView(ListView):
    model = Employee
    template_name = "employee/employees_list.html"
    context_object_name = 'employees'


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = "employee/employee_details.html"
    context_object_name = 'employee'


class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = "employee/employee_update.html"
    form_class = EmployeeForm
    success_url = reverse_lazy('employee_app:employees_list')


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = "employee/employee_delete.html"
    context_object_name = 'employee'
    success_url = reverse_lazy('employee_app:employees_list')


class EmployeeCreateView(CreateView):
    model = Employee
    template_name = "employee/employee_create.html"
    form_class = EmployeeForm
    success_url = reverse_lazy('employee_app:employees_list')


class EmployeesByDepartmentListView(ListView):
    model = Employee
    template_name = "employee/employees_by_department.html"
    context_object_name = 'employees'

    def get_queryset(self):
        department_short_name = self.kwargs['short_name']
        queryset = Employee.objects.filter(
            department__short_name=department_short_name
        )
        return queryset
