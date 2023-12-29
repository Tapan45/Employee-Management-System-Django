from django.shortcuts import render , get_object_or_404 , redirect,HttpResponseRedirect,HttpResponse
from django.db.models import Q                
from .models import Employee_Table,SalaryDetails,Holiday,Attendance
from django.views.decorators.http import require_POST
from django.contrib import messages

from decimal import Decimal, InvalidOperation

from django.core.exceptions import ValidationError

import random
from random import randrange
def fun(request):
    return render(request,"index.html")


from .models import Employee_Table
def emp_function(request):
    if request.method=='POST':
        name=request.POST.get('emp_name')
        designation=request.POST.get('emp_designation')
        number=request.POST.get('emp_num')
        email=request.POST.get('emp_email')
        address=request.POST.get('emp_address')
        state=request.POST.get('emp_state')
        city=request.POST.get('emp_city')
        pincode=request.POST.get('emp_pincode')
        salary=request.POST.get('emp_salary')
        field=request.POST.get('emp_field')
        image=request.FILES.get('emp_image')
        print(image)
       
        
        
        Employee_Table.objects.create(
         
            employee_name = name,
            employee_designation = designation,
            employee_phn_num = number,
            employee_email = email,
            employee_address = address,
            employee_state = state,
            employee_city = city,
            employee_pincode = pincode,
            employee_salary = salary,
            employee_field = field,
            employee_image= image
            
        )
    return render(request,"add_emp_details.html")

def show_all_employees(request):
    if 'search' in request.GET:
        search_click = request.GET['search']
       # employees = Employee_Table.objects.filter(employee_name__icontains=search_click)
        multiple_search =Q(Q(employee_name__icontains=search_click)|Q(employee_id__icontains=search_click))
        employees=Employee_Table.objects.filter(multiple_search)
    else:
        employees = Employee_Table.objects.all()
    context = {
        "Employee_list": employees
    }
    return render(request, "all_employee_list.html", context)




def all_employee_detail(request, id):
    
    employees = Employee_Table.objects.filter(pk = id)

    context = {
        "employees" : employees
    } 
    return render(request ,"show_all_details.html",context)


def update_employee(request,employee_id):
    
    employee =get_object_or_404(Employee_Table , id = employee_id) 
    
    if request.method == 'POST':
        
        updated_name=request.POST.get('emp_name')
        updated_designation=request.POST.get('emp_designation')
        updated_number=request.POST.get('emp_num')
        updated_email=request.POST.get('emp_email')
        updated_address=request.POST.get('emp_address')
        updated_state=request.POST.get('emp_state')
        updated_city=request.POST.get('emp_city')
        updated_pincode=request.POST.get('emp_pincode')
        updated_salary=request.POST.get('emp_salary')
        updated_field=request.POST.get('emp_field')
        update_image=request.FILES.get('emp_image')
        
        employee.employee_name = updated_name
        employee.employee_designation = updated_designation
        employee.employee_phn_num = updated_number
        employee.employee_email = updated_email
        employee.employee_address = updated_address
        employee.employee_state = updated_state
        employee.employee_city = updated_city
        employee.employee_pincode = updated_pincode
        employee.employee_salary = updated_salary
        employee.employee_field = updated_field
        employee.employee_image = update_image
        employee.save()
        
        return redirect('empemployee_list')
        
        
    context = {
        "employee" : employee
    }
    
    return render(request , "update_employee.html", context)
    


def delete_employee(request, employee_id):
    object = get_object_or_404(Employee_Table, id=employee_id)
    object.delete()
    return redirect('empemployee_list')













def salary_calculation_view(request):
    if request.method == 'POST':
        try:
            
            employee_name = request.POST.get('employeeName')
            basic = Decimal(request.POST.get('basic', '0').replace(',', ''))
            hra = Decimal(request.POST.get('hra', '0').replace(',', ''))
            others = Decimal(request.POST.get('others', '0').replace(',', ''))
            conv = Decimal(request.POST.get('conv', '0').replace(',', ''))
            max_epf_wages = Decimal(request.POST.get('maxEpfWages', '0').replace(',', ''))
            max_esi_wages = Decimal(request.POST.get('maxEsiWages', '0').replace(',', ''))
            lta = Decimal(request.POST.get('lta', '0').replace(',', ''))
            medical = Decimal(request.POST.get('medical', '0').replace(',', ''))
            rest_allow = Decimal(request.POST.get('restAllow', '0').replace(',', ''))
            gross_salary = Decimal(request.POST.get('grossSalary', '0').replace(',', ''))
            net_pay = Decimal(request.POST.get('netPay', '0').replace(',', ''))
            ctc = Decimal(request.POST.get('ctc', '0').replace(',', ''))
            employee_epf = Decimal(request.POST.get('employeeEpf', '0').replace(',', ''))
            employee_esi = Decimal(request.POST.get('employeeEsi', '0').replace(',', ''))
            employer_epf = Decimal(request.POST.get('employerEpf', '0').replace(',', ''))
            employer_esi = Decimal(request.POST.get('employerEsi', '0').replace(',', ''))

            # Create SalaryDetails instance with validated data
            SalaryDetails(
                employee_name=employee_name,
                basic=basic,
                hra=hra,
                others=others,
                conv=conv,
                max_epf_wages=max_epf_wages,
                max_esi_wages=max_esi_wages,
                lta=lta,
                medical=medical,
                rest_allow=rest_allow,
                gross_salary=gross_salary,
                net_pay=net_pay,
                ctc=ctc,
                employee_epf=employee_epf,
                employee_esi=employee_esi,
                employer_epf=employer_epf,
                employer_esi=employer_esi,
                # Assign other validated fields here
                # ...
            )
            
        except InvalidOperation as e:
            # Handle the error, such as displaying an error message or redirecting to a page
            error_message = f"Invalid input: {str(e)}"
           

       

    
    employees = Employee_Table.objects.all()
    context = {
        'employees': employees
    }
    return render(request, 'add_salary.html', context)






def view_salary(request):
    return render (request,'view_salary.html')



def attendance_process(request):
    employees = Employee_Table.objects.all()  
    context = {
        'employees': employees  
     }
    if request.method == 'POST':
        employee_name = request.POST['employeeName']
        start_day = request.POST['startDay']
        end_day = request.POST['endDay']

        try:
            attendance = Attendance.objects.create(
                employee_name=employee_name,
                start_day=start_day,
                end_day=end_day
            )
            attendance.save()
            messages.success(request, 'Attendance details added successfully')
        except Exception as e:
            messages.error(request, f'Error: {e}')

    return render(request, 'process_attendance.html',context)













def create_holidays(request):
    if request.method == 'POST':
        start_day = request.POST.get('startDay')
        end_day = request.POST.get('endDay')
        holiday_name = request.POST.get('holidayName')

      
        print(f"Start Day: {start_day}, End Day: {end_day}, Holiday Name: {holiday_name}")
        
        
        Holiday.objects.create (
            
             start_day = start_day ,
             end_day =  end_day,
             holiday_name =  holiday_name 
            
            
            
            
         
           
        ) 
        
        
        
        
        
        
        
        

       
        #return HttpResponse("Holiday created successfully!") 
        return redirect ('create_holidays')

    return render(request, 'create_holidays.html') 
