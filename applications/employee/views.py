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
