from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ClassName, Student, Attendance
from .forms import ClassNameForm, StudentForm, AttendanceForm
from django.db import IntegrityError
from django_xhtml2pdf.utils import generate_pdf
from django.utils import timezone


from django.db.models import Avg, Max, Min, Sum, Count
# Create your views here.


@login_required()
def classNames(request):
    context = {}
    qs = ClassName.objects.all()
    context['page'] = 'Class Names'
    context['queryset'] = qs
    return render(request, 'administration/class_list.html', context)


@login_required()
def students(request):
    context = {}
    qs = Student.objects.all()
    context['page'] = 'Students'
    context['queryset'] = qs
    return render(request, 'administration/students.html', context)


@login_required()
def attendances(request):
    context = {}
    qs = Attendance.objects.filter(report='no')
    context['page'] = 'Attendances'
    context['queryset'] = qs
    return render(request, 'administration/attendances.html', context)


@login_required()
def edit_class_name(request, pk= None):
    context = {}
    if pk:
        class_name = ClassName.objects.get(pk=pk)
        form = ClassNameForm(request.POST or None, instance=class_name)
    else:
        form = ClassNameForm(request.POST or None)

    if form.is_valid():
        try:
            if not pk:

                class_name = form.save(commit=False)
                class_name.save()
                messages.success(request, 'Class name created')

            else:
                class_name = form.save(commit=False)
                class_name.save()
                messages.success(request, 'Class name  updated')

            return redirect('classNames')
        except IntegrityError as err:
            err = messages.error(request, 'This data already exists in the database')

    context['form'] = form
    context['pk'] = pk
    context['parent'] = 'Admin'
    context['add_page'] = 'Add class name'
    context['edit_page'] = 'Edit class name'
    return render(request, 'administration/edit_class_name.html', context)


@login_required()
def edit_student(request, pk= None):
    context = {}
    if pk:
        student = Student.objects.get(pk=pk)
        form = StudentForm(request.POST or None, instance=student)
    else:
        form = StudentForm(request.POST or None)

    if form.is_valid():
        if not pk:
            student = form.save(commit=False)
            # student.created_by_id = request.user.id
            student.save()
            messages.success(request, 'student created')

        else:
            learner = form.save(commit=False)
            learner.save()
            messages.success(request, 'student  updated')

        return redirect('students')

    context['form'] = form
    context['pk'] = pk
    context['parent'] = 'Admin'
    context['add_page'] = 'Add student'
    context['edit_page'] = 'Edit student'
    return render(request, 'administration/edit_student.html', context)


@login_required()
def edit_attendance(request, pk= None):
    context = {}
    if pk:
        attendance = Attendance.objects.get(pk=pk)
        form = AttendanceForm(request.POST or None, instance=attendance)
    else:
        form = AttendanceForm(request.POST or None)

    if form.is_valid():
        try:
            if not pk:
                attendance = form.save(commit=False)
                # attendance.created_by_id = request.user.id
                attendance.save()
                messages.success(request, 'attendance created')

            else:
                attendance = form.save(commit=False)
                attendance.save()
                messages.success(request, 'attendance  updated')

            return redirect('attendances')

        except IntegrityError as e:
            e = messages.error(request, 'This data already exists in the databases')

    context['form'] = form
    context['district'] = pk
    context['parent'] = 'Admin'
    context['add_page'] = 'Add attendance'
    context['edit_page'] = 'Edit attendance'
    return render(request, 'administration/edit_attendance.html', context)


@login_required()
def delete_class_name(request, pk):
    context = {}
    qs = ClassName.objects.filter(pk=pk).update(deleted=True)
    messages.success(request, 'class name deleted')
    return redirect('classNames')


@login_required()
def delete_student(request, pk):
    context = {}
    qs = Student.objects.filter(pk=pk).update(deleted=True)
    messages.success(request, 'student deleted')
    return redirect('students')


@login_required()
def delete_attendance(request, pk):
    context = {}
    qs = Attendance.objects.filter(pk=pk).update(deleted=True)
    messages.success(request, 'attendance deleted')
    return redirect('attendances')


@login_required()
def report_student(request, pk):
    context = {}
    qs = Attendance.objects.filter(pk=pk).update(report='yes')
    messages.success(request, 'student attendance reported')
    return redirect('attendances')


@login_required()
def term_reports(request):
    context = {}
    qs = Student.objects.all()
    context['page'] = 'Term Reports'
    context['queryset'] = qs
    return render(request, 'administration/term_reports.html', context=context)


def generate_pdf_report(response, pk, term):

    context = {}
    student = Student.objects.get(pk=pk)
    absent_count = Attendance.objects.filter(student_id=pk, status='absent', term=term, report='yes').count()
    presence_count = Attendance.objects.filter(student_id=pk, status='present', term=term, report='yes').count()

    context['rpt_name'] = "CSG School Report"
    context['term'] = term
    context['absent_count'] = absent_count
    context['absent_count'] = absent_count
    context['presence_count'] = presence_count
    context['name'] = student.full_name
    context['grade'] = student.class_name.grade
    context['class_name'] = student.class_name.name
    context['today'] = timezone.now()

    resp = HttpResponse(content_type='application/pdf')
    result = generate_pdf('administration/student_report_pdf.html', file_object=resp, context=context)
    return result