from django.test import TestCase
from django.shortcuts import resolve_url as r
from aditamento.militaries.models import Military



class MilitaryViewListTest(TestCase):
    def setUp(self):
        self.obj = Military.objects.create(name='Levi', cpf='12345678901')
        self.resp = self.client.get(r('militaries:list'))
    
    def test_get(self):
        self.assertTrue(200, self.resp.status_code)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'militaries/military_list.html')

    def test_context(self):
        militaries = self.resp.context['militaries']
        self.assertListEqual(list(militaries), [self.obj])
    
    def test_html(self):
        contents = (self.obj.name, self.obj.cpf, )

        with self.subTest():
            for expected in contents:
                self.assertContains(self.resp, expected)