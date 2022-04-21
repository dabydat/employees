from django.urls import path
from . import views

app_name = 'department_app'

urlpatterns = [
    path('departments_list/',
         views.DepartmentListView.as_view(),
         name='departments_list'
         ),
    path('new_department/',
         views.NewDepartmentCreateView.as_view(),
         name='new_department'
         )

]
