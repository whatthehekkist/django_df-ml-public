# from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from employees.models import Employee
from employees.forms import UpdateForm, DeleteForm, InsertForm


def delete_emp_view(request, emp_id):
    employee = get_object_or_404(Employee, id=emp_id)
    if request.method == 'POST':
        employee.delete()
        return redirect(reverse('employees:index'))

    else:
        form = DeleteForm(instance=employee)

    return render(request, 'employees/delete.html', {'form': form})


def edit_emp_view(request, emp_id):
    employee = get_object_or_404(Employee, id=emp_id)

    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect(reverse('employees:index'))
    else:
        form = UpdateForm(instance=employee)

    return render(request, 'employees/update.html', {'form': form})


def extract_employee(request):

    # employees = Employee.objects.all()
    employees = Employee.objects.all().order_by('id').values()

    paginator = Paginator(employees, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST':
        form = InsertForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('employees:index'))
    else:
        form = InsertForm()

    return render(request, 'employees/index.html', {'page_obj': page_obj, 'form': form})





