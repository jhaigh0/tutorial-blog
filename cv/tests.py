from __future__ import unicode_literals
from django.test import TestCase

class CVMainPageTest(TestCase):

    def test_cv_main_uses_template(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'cv_main.html')
