from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from ManageEmployees.settings import BASE_DIR, MEDIA_ROOT, MEDIA_URL
from employee.forms import EmployeeForm
from employee.models import Employee


# Create your views here.

class EmployeeDetailView(View):

    def get(self, request, pk):
        employee = Employee.objects.filter(pk=pk).first()
        print(employee.photo)

        return render(request, 'employee_detail.html',
                      context={'employee': employee})

class EmployeeListView(View):
    employees = Employee.objects.all()
    def get(self, request):
        return render(request, 'employee_list.html',
                      context={'employees': self.employees})


class CreateEmployeeView(View):
    def get(self, request):
        form = EmployeeForm()
        return render(request, 'employee_form.html',
                      context={'form': form})

    def post(self, request):
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            emp = Employee()
            emp.first_name = form.cleaned_data['first_name']
            emp.last_name = form.cleaned_data['last_name']
            emp.email = form.cleaned_data['email']
            emp.date_birth = form.cleaned_data['date_birth']
            emp.photo = form.cleaned_data['photo']
            emp.save()
            return HttpResponse('Employee created successfully!')
        else:
            return HttpResponse('Invalid data!')