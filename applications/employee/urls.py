from django.urls import path
from . import views

app_name = 'employee_app'

urlpatterns = [
    path(
        '',
        views.IndexTemplateView.as_view(),
        name='index'
    ),
    path(
        'employees/',
        views.EmployeeListView.as_view(),
        name='employees_list'
    ),
    path(
        'employee/<pk>',
        views.EmployeeDetailView.as_view(),
        name='employee_details'
    ),
    path(
        'employee_update/<pk>',
        views.EmployeeUpdateView.as_view(),
        name='employee_update'
    ),
    path(
        'employee_delete/<pk>',
        views.EmployeeDeleteView.as_view(),
        name='employee_delete'
    ),
    path(
        'employee_create/',
        views.EmployeeCreateView.as_view(),
        name='employee_create'
    ),
]
