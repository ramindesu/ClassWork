from django.db import models
from datetime import date
from django.core.validators import MinValueValidator 


# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=255,db_index=True,unique=True)
    date_birth = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        ordering = ['last_name']


class Teacher(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(blank=True,null=True,unique=True)
    hired_date = models.DateField(default=date.today)
    is_teaching = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
        ordering = ['full_name']



class Course(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=255)
    started_date = models.DateField(default=date.today)
    credits = models.PositiveSmallIntegerField(default=3 ,validators=[MinValueValidator(1)])
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ['title']


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_of_enrollment = models.DateField(default=date.today)
    grade = models.DecimalField(max_digits=5, decimal_places=3)

    class Meta:
        verbose_name = 'Enrollment'
        verbose_name_plural = 'Enrollment'






        