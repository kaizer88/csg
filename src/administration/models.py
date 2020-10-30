from django.db import models
from libs.models import BaseModel
from django.contrib.auth.models import User

# Create your models here.


class ClassName(BaseModel):
    GRADES = (
        ('10', '10'),
        ('11', '11'),
        ('12', '12')
    )
    name = models.CharField(max_length=255, null=False, blank=False)
    code = models.CharField(max_length=5, unique=True, null=False, blank=False)
    grade = models.CharField(max_length=250, choices=GRADES, null=False, blank=False)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        unique_together = ('name', 'grade','deleted',)

    def __str__(self):
        return "{} - {}".format(self.name, self.grade)


class Student(BaseModel):

    student_number = models.CharField(max_length=255, unique=True, null=False, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    surname = models.CharField(max_length=255, null=False, blank=False)
    id_number = models.IntegerField(null=False, blank=False)
    class_name = models.ForeignKey(ClassName, on_delete=models.CASCADE, null=False, blank=False)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return "{} - {} - {}".format(self.name, self.surname, self.class_name)

    @property
    def full_name(self):
        return "{} {}".format(self.name, self.surname)

    @property
    def std(self):
        return "{}".format(self.student_number)


class Attendance(BaseModel):
    STATUES = (
        ('absent', 'Absent'),
        ('present', 'Present')
    )
    Reported = (
        ('no', 'No'),
        ('yes', 'Yes')
    )
    TERMS = (
        ('1', '1st'),
        ('2', '2nd'),
        ('3', '3rd'),
        ('4', '4th')
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False, blank=False)
    day = models.DateField(null=False, blank=False)
    time = models.TimeField(null=True, blank=True)
    status = models.CharField(max_length=250, choices=STATUES, null=False, blank=False)
    report = models.CharField(max_length=250, choices=Reported, null=False, blank=False, default='no')
    term = models.CharField(max_length=255, choices=TERMS, null=True, blank=True)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        unique_together = ('student', 'day',)

    def __str__(self):
        return self.student

