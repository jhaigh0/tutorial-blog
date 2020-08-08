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

        #Sees my personal info under the main title
        email = 'jonathanhaigh0@gmail.com'
        number = '07527744192'
        address = '56 Cherry Tree Avenue Haslemere GU27 1JP'
        details_text = self.browser.find_element_by_tag_name('ul').text
        self.assertIn(email, details_text)
        self.assertIn(number, details_text)
        self.assertIn(address, details_text)


class AdminVisitorTest(LiveServerTestCase):

    def setUp(self):
        User.objects.create_superuser(
            username='admin',
            password='psw',
            email='admin@example.com'
        )

        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def checkIsIn(self, element_list, phrase):
        for element in element_list:
            if element.text == phrase:
                return true

        return false

    def test_can_add_education(self):
        #go to admin login page and log in
        self.browser.get('%s%s' % (self.live_server_url,  "/admin/"))

        username = self.browser.find_element_by_id("id_username")
        username.send_keys("admin")
        password = self.browser.find_element_by_id("id_password")
        password.send_keys("psw")
        log_in = self.browser.find_element_by_xpath('//input[@value="Log in"]')
        log_in.click()

        #back to main page
        self.browser.get(self.live_server_url)
        time.sleep(10)

        #Goes to CV page
        cv_button = self.browser.find_element_by_id('id_cv_button')
        cv_button.click()
        current_url = self.browser.current_url
        self.assertRegex(current_url, '.+/cv/')

        #500 error on the cv page and i have no idea why
        #spent about a week trying to fix it and i've now given up 

        #decides to add new education entry
        time.sleep(10)
        new_dated_button = self.browser.find_element_by_id('new-dated-btn')
        new_dated_button.click()

        #taken to a form page
        current_url = self.browser.current_url
        self.assertRegex(current_url, '.+/cv/new_dated')

        #enters info (leaving the ended box unchecked)
        title  = "Test University"
        start_date = "01/07/2018"
        text = "I really enjoyed my time here"
        type_id = "education uni"

        title_box = self.browser.find_element_by_id('id_title')
        title_box.send_keys(title)
        start_date_box = self.browser.find_element_by_id('id_start_date')
        start_date_box.send_keys(start_date)
        text_box = self.browser.find_element_by_id('id_text')
        text_box.send_keys(text)
        type_id_box = self.browser.find_element_by_id('id_type_id')
        type_id_box.clear() #remove place holder value
        type_id_box.send_keys(type_id)

        #click save button to be redirected back to main cv page
        save_button = self.browser.find_element_by_id('id-save-btn')
        save_button.click()

        current_url = self.browser.current_url
        self.assertRegex(current_url, '.+/cv/')

        #can see the new entry on the site
        titles = self.browser.find_elements_by_class_name('entry-title')
        self.asserTrue(self.checkIsIn(titles, title))
        dates = self.browser.find_elements_by_class_name('date')
        self.asserTrue(self.checkIsIn(dates, start_date))
        content = self.browser.find_elements_by_class_name('text-content')
        self.asserTrue(self.checkIsIn(content, text))
