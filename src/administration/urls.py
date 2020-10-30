from django.urls import path
from .views import classNames, students, attendances
from .views import edit_class_name, edit_student, edit_attendance
from .views import delete_class_name, delete_student, delete_attendance
from .views import report_student, term_reports, generate_pdf_report


urlpatterns = [

    path('classNames', classNames, name='classNames'),
    path('students', students, name='students'),
    path('attendances', attendances, name='attendances'),

    path('add_class_name', edit_class_name, name='add_class_name'),
    path('add_student', edit_student, name='add_student'),
    path('add_attendance', edit_attendance, name='add_attendance'),

    path('edit_class_name/<pk>', edit_class_name, name='edit_class_name'),
    path('edit_student/<pk>', edit_student, name='edit_student'),
    path('edit_attendance/<pk>', edit_attendance, name='edit_attendance'),

    path('delete_class_name/<pk>', delete_class_name, name='delete_class_name'),
    path('delete_student/<pk>', delete_student, name='delete_student'),
    path('delete_attendance/<pk>', delete_attendance, name='delete_attendance'),

    path('report_student/<pk>', report_student, name='report_student'),
    path('term_reports', term_reports, name='term_reports'),
    path('generate_pdf_report/<pk>/<term>', generate_pdf_report, name='generate_pdf_report'),


]
