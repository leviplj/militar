from django.test import TestCase


class MilitaryTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/military/')

    def test_get(self):        
        self.assertEquals(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'militaries/military_list.html')