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
        'employees/<pk>',
        views.EmployeeDetailView.as_view(),
        name='employee_details'
    ),
]
