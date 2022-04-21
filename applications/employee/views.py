from django.shortcuts import render
from .models import Employee
from django.views.generic import (TemplateView,
                                  ListView
                                  )

# Create your views here.


class IndexTemplateView(TemplateView):
    template_name = "index.html"


class EmployeeListView(ListView):
    model = Employee
    template_name = "employee/employees_list.html"
    context_object_name = 'employees'
