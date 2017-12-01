from django.test import TestCase
from aditamento.militaries.models import Military
from datetime import datetime


class MilitaryModelTest(TestCase):
    def setUp(self):
        self.obj = Military(name='Levi', cpf='12345678901')
        self.obj.save()

    def test_create(self):
        self.assertTrue(Military.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.create_at, datetime)

    def test_str(self):
        self.assertEqual('Levi', str(self.obj))