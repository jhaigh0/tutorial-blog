from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User
import time

class NoramlVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_sees_sight_correctly(self):
        #A user decides to visit the CV site
        self.browser.get(self.live_server_url)

        #Sees the button labled CV
        cv_button = self.browser.find_element_by_id('id_cv_button')
        self.assertEqual(cv_button.get_attribute('class'), 'cv_Button')

        #Clicks on the CV button and is taken to the cv site
        cv_button.click()
        current_url = self.browser.current_url
        self.assertRegex(current_url, '.+/cv/')

        #Sees that the title and header mention CVs
        self.assertIn('CV', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('CV', header_text)


class AdminVisitorTest(LiveServerTestCase):

    def setUp(self):
        User.objects.create_superuser(
            username='admin',
            password='admin',
            email='admin@example.com'
        )

        self.browser = webdriver.Firefox()

        self.browser.get('%s%s' % (self.live_server_url,  "/admin/"))

        username = self.browser.find_element_by_id("id_username")
        username.send_keys("admin")
        password = self.browser.find_element_by_id("id_password")
        password.send_keys("admin")

        self.browser.get(self.live_server_url)


    def tearDown(self):
        self.browser.quit()

    def test_can_add_education(self):
        time.sleep(10)
