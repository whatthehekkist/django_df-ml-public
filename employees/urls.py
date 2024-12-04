from django.urls import path
from employees import views


app_name = "employees"
urlpatterns = [
    # path('test/', views.test_view, name='test'),
    # path('response/<str:name>/', views.response_view, name='response'),
    path('', views.extract_employee, name='index'),
    path('edit/<int:emp_id>/', views.edit_emp_view, name='edit'),
    path('delete/<int:emp_id>/', views.delete_emp_view, name='delete'),
]
