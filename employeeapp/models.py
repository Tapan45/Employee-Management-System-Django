from django.db import models
import random


 
 
class Employee_Table(models.Model):
      
    employee_name = models.CharField(max_length=50)
    employee_designation = models.CharField(max_length=50)
    employee_phn_num = models.CharField(max_length=10) 
    employee_email = models.EmailField()
    employee_address = models.CharField(max_length=200)
    employee_state = models.CharField(max_length=50)
    employee_city = models.CharField(max_length=50)
    employee_pincode = models.CharField(max_length=6)  
    employee_salary = models.DecimalField(max_digits=10, decimal_places=2)  
    employee_field = models.CharField(max_length=100)
    employee_image = models.ImageField(upload_to='documents/',blank=True)
    employee_id = models.BigIntegerField(unique=True)
    

    def save(self, *args, **kwargs):
       while True:
           random_number = random.randint(10**11 , 10**12 - 1)
           if not Employee_Table.objects.filter(employee_id = random_number).exists():
               self.employee_id = random_number
               break
       super(Employee_Table , self).save(*args, **kwargs)
       
       
       

class SalaryDetails(models.Model):
    employee_name = models.CharField(max_length=100)
    basic = models.DecimalField(max_digits=10, decimal_places=2)
    hra = models.DecimalField(max_digits=10, decimal_places=2)
    others = models.DecimalField(max_digits=10, decimal_places=2)
    conv = models.DecimalField(max_digits=10, decimal_places=2)
    max_epf_wages = models.DecimalField(max_digits=10, decimal_places=2)
    max_esi_wages = models.DecimalField(max_digits=10, decimal_places=2)
    lta = models.DecimalField(max_digits=10, decimal_places=2)
    medical = models.DecimalField(max_digits=10, decimal_places=2)
    rest_allow = models.DecimalField(max_digits=10, decimal_places=2)
    gross_salary = models.DecimalField(max_digits=10, decimal_places=2)
    net_pay = models.DecimalField(max_digits=10, decimal_places=2)
    ctc = models.DecimalField(max_digits=10, decimal_places=2)
    employee_epf = models.DecimalField(max_digits=10, decimal_places=2)
    employee_esi = models.DecimalField(max_digits=10, decimal_places=2)
    employer_epf = models.DecimalField(max_digits=10, decimal_places=2)
    employer_esi = models.DecimalField(max_digits=10, decimal_places=2)

    

    def __str__(self):
        return f"{self.employee_name} - Basic: {self.basic}, HRA: {self.hra}"







class Holiday(models.Model):
    start_day = models.DateField()
    end_day = models.DateField()
    holiday_name = models.CharField(max_length=100)

    def __str__(self):
        return self.holiday_name
    



class Attendance(models.Model):
    employee_name = models.CharField(max_length=100)
    start_day = models.DateField()
    end_day = models.DateField()

    def __str__(self):
        return self.employee_name
