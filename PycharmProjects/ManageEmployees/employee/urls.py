from django.urls import path

from employee.views import EmployeeListView, CreateEmployeeView, EmployeeDetailView

urlpatterns = [
    path('new/', CreateEmployeeView.as_view(), name='employee-new'),
    path('list/', EmployeeListView.as_view(), name='employee-list'),
    path('detail/<int:pk>', EmployeeDetailView.as_view(), name='employee-list'),
]