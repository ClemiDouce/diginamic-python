import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class AvosclicsTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("./chromedriver.exe")
        self.addCleanup(self.browser.quit)

    def test_page_title(self):
        self.browser.get('http://a-vos-clics-formation.fr/')
        self.assertIn('@ Vos Clics', self.browser.title)
