# Django imports
from django.test import TestCase
from django.test.client import RequestFactory, Client
from django.contrib.auth.models import AnonymousUser


# Local Django imports
from exam.views import UpdateCustomExam
from exam.models import CustomExam
from user.models import User, Patient, HealthProfessional


class UpdateCustomExamsViewTest(TestCase):
    """
    Testing methods of Class CreateCustomExamsView.
    """
    def setUp(self):
        self.factory = RequestFactory()
        self.health_professional = HealthProfessional.objects.create_user(email='doctor@doctor.com', password='senha12')
        self.patient = Patient.objects.create_user(email='patient@patient.com', password='senha12')

        self.description = "Examina alguma coisa"
        self.name = "Alguma coisa"

        custom_exam = CustomExam()
        custom_exam.name = "Invalido"
        custom_exam.description = "Alguma descricao"
        custom_exam.health_professional_FK = self.health_professional
        custom_exam.pk = 1
        custom_exam.save()

    # Testing view calls
    def test_get_without_login(self):
        request = self.factory.get('/exam/update_custom_exams/1/')
        request.user = AnonymousUser()

        response = UpdateCustomExam.as_view()(request)
        self.assertEqual(response.status_code, 302)

    def test_get_with_patient(self):
        request = self.factory.get('/exam/update_custom_exams/1/')
        request.user = self.patient

        response = UpdateCustomExam.as_view()(request)
        self.assertEqual(response.status_code, 302)

    '''def test_get_with_health_professional(self):
        request = self.factory.get('/exam/update_custom_exams/1/')
        request.user = self.health_professional

        response = UpdateCustomExam.as_view()(request)
        self.assertEqual(response.status_code, 200)'''

    # Testing method 'post' in UpdateCustomExam.
    def test_post_without_login(self):
        request = self.factory.post('/exam/update_custom_exams/1/',
                                    {'name': self.name, 'description': self.description})
        request.user = AnonymousUser()

        response = UpdateCustomExam.as_view()(request)
        self.assertEqual(response.status_code, 302)

    def test_post_with_patient(self):
        request = self.factory.post('/exam/update_custom_exams/1/',
                                    {'name': self.name, 'description': self.description})
        request.user = self.patient

        response = UpdateCustomExam.as_view()(request)
        self.assertEqual(response.status_code, 302)

    '''def test_post_with_health_professional(self):
        request = self.factory.post('/exam/update_custom_exams/1/',
                                    {'name': self.name, 'description': self.description})
        request.user = self.health_professional

        response = UpdateCustomExam.as_view()(request)
        self.assertEqual(response.status_code, 200)'''
