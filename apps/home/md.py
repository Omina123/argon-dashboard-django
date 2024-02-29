from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100,blank=True, null= True)
    description = models.TextField()
    objects=models.Manager()
class Program (models.Model):
    name=models.CharField(max_length= 250, blank=True, null=True)
    department= models.ForeignKey(Department, on_delete= models.CASCADE)
    objects=models.Manager()
class Lecturer(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,blank=True, null= True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    email = models.EmailField()
    
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    objects=models.Manager()
class AcademicYear(models.Model):
    name = models.CharField(max_length=100,blank=True, null= True)
    start_date = models.DateField()
    end_date = models.DateField()
    objects=models.Manager()  
class Semester(models.Model):
    name = models.CharField(max_length=100)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    objects=models.Manager()
class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    id= models.AutoField(primary_key=True)
    surname = models.CharField(max_length=100, blank=True, null= True)
    first_name = models.CharField(max_length=100, blank=True, null= True)
    last_name = models.CharField(max_length=100, blank=True, null= True)
    admission_number = models.CharField(max_length=30, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    address = models.TextField()
    program=models.ForeignKey(Program,on_delete= models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    objects =models.Manager()
class Unit(models.Model):
    id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,blank=True, null= True)
    code = models.CharField(max_length=10, unique=True,blank=True, null= True)
    credits = models.IntegerField()
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    program=models.ForeignKey(Program,on_delete= models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    student= models.Foreignkey(Student, on_delete=models.CASCADE)
    objects=models.Manager()


    # Add more fields as needed

class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,blank=True, null= True)
    email = models.EmailField()
    objects  = models.Manager()

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=5, decimal_places=2)
    # Add more fields as needed

class ICT(models.Model):
    id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,blank=True, null= True)
    contact_person = models.CharField(max_length=100,blank=True, null= True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    objects=models.Manager()
    # Add more fields as needed
