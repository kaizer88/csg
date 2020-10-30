
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "csgschool.settings")

from django.test import TestCase
from .models import ClassName, Student, Attendance


# Create your tests here.

# models test
class ModelTest(TestCase):

    def create_class_name(self, name="maths", code="eng10", grade='10'):
        return ClassName.objects.create(name=name, code=code, grade=grade)

    def create_student(self, student_number="12345", name="lukhanyo", middle_name="theo",
                       surname="magwentshu", id_number=123456, class_name_id=1):
        return Student.objects.create(student_number=student_number, name=name, middle_name=middle_name,
                                      surname=surname, id_number=id_number, class_name_id=class_name_id)

    def test_model_creation(self):
        w = self.create_class_name()
        w2 = self.create_student()
        self.assertTrue(isinstance(w, ClassName))
        self.assertTrue(isinstance(w2, Student))
        self.assertEqual(w.__str__(), w.name,w.grade)
        self.assertEqual(w2.__str__(), w2.name, w2.surname,w2.class_name)

if __name__ == '__main__':
    run = ModelTest()
    run.test_model_creation()
