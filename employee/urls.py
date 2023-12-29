"""
URL configuration for employee project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from employeeapp import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.fun,name="index"),
    path('emp/det',views.emp_function,name="emp_det"),
    path('emp/list',views.show_all_employees,name="empemployee_list"),
    path('allemp/list/<int:id>/',views.all_employee_detail,name="allemp_list"),
    path('edit_employee/<int:employee_id>/', views.update_employee, name='edit_employee'),
    path('delete_employee/<int:employee_id>/', views.delete_employee, name='delete_employee'),
    path('salary',views.salary_calculation_view,name="add_salary"),
           path('view_salary/',views.view_salary, name='view_salary'),
      path('create/', views.create_holidays, name='create_holidays'),
        path('attendance-process/', views.attendance_process, name='attendance_process'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)