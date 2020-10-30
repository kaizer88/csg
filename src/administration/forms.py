from django import forms
from .models import ClassName, Student, Attendance


class ClassNameForm(forms.ModelForm):
    class Meta:
        model = ClassName
        fields = ['name', 'code', 'grade']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_number', 'name', 'middle_name',
                  'surname', 'id_number', 'class_name']

class DateInput(forms.DateInput):
    input_type = 'date'

class AttendanceForm(forms.ModelForm):
    day = forms.DateField(widget=DateInput())
    class Meta:
        model = Attendance
        fields = ['student', 'day', 'status']
