from __future__ import unicode_literals
from django.test import TestCase
from .models import CV_Element

class CVMainPageTest(TestCase):

    def test_cv_main_uses_template(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'cv_main.html')

    def test_db_items_display_properly(self):
        intro_test = CV_Element()
        intro_test.text = 'this is the intro paragraph'
        intro_test.type_id = 'intro new'
        intro_test.save()
