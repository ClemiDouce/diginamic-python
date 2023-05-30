import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

tuple_dico = {"css": By.CSS_SELECTOR, "name": By.NAME, "link": By.LINK_TEXT, "class": By.CLASS_NAME}


def get_tuple_search(search):
    if search.startswith("//"):
        search_tuple = (By.XPATH, search)
    else:
        key = tuple_dico.get(search.split(":")[0])
        search_tuple = (key, search.split(":")[1])
    return search_tuple


class OrangeIHMTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("./chromedriver.exe")
        self.wait = WebDriverWait(self.browser, 10)
        self.addCleanup(self.browser.quit)

    def wait_and_type(self, search: str, input: str):
        self.wait.until(EC.presence_of_element_located(get_tuple_search(search))).send_keys(input)

    def wait_and_click(self, search: str):
        self.wait.until(EC.presence_of_element_located(get_tuple_search(search))).click()

    def wait_until_eleme_showed(self, search: str):
        elem = self.wait.until(EC.presence_of_element_located(get_tuple_search(search)))
        if elem:
            return True
        return False

    def wait_and_get(self, search: str) -> WebElement:
        return self.wait.until(EC.presence_of_element_located(get_tuple_search(search)))

    def test_login(self):
        self.browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        self.wait_and_type("name:username", "Admin")
        self.wait_and_type("name:password", "admin123")
        self.wait_and_click("//button[@type='submit']")
        self.assertTrue(self.wait_until_eleme_showed("//div[@id='app']/div/div/header/div/div[2]/ul/li/span/p"))

    def test_logout(self):
        self.test_login()
        self.wait_and_click("//div[@id='app']/div/div/header/div/div[2]/ul/li/span/p")
        self.wait_and_click("link:Logout")
        self.assertTrue(self.wait_until_eleme_showed("name:username"))

    def test_login_ko(self):
        self.browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        self.wait_and_type("name:username", "AdminWrong")
        self.wait_and_type("name:password", "admin123")
        self.wait_and_click("//button[@type='submit']")
        self.assertTrue(self.wait_until_eleme_showed("class:oxd-alert--error"))

    def test_add_employe(self):
        self.test_login()
        self.wait_and_click("//div[@id='app']/div/div/aside/nav/div[2]/ul/li[2]/a/span")
        self.wait_and_click("link:Employee List")
        self.wait_and_click("//div[@id='app']/div/div[2]/div[2]/div/div[2]/div/button")
        self.wait_and_type("name:firstName", "martin")
        self.wait_and_type("name:middleName", "middle")
        self.wait_and_type("name:lastName", "ofcourse")
        self.wait_and_type("//div[@id='app']/div/div[2]/div[2]/div/div/form/div/div[2]/div/div[2]/div/div/div[2]/input",
                           "223344")
        self.wait_and_click("//button[@type='submit']")
        self.wait_and_click(
            "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[3]/div/div/div/div[2]/div/div/div")
        self.wait_and_click(
            "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[3]/div/div/div/div[2]/div/div/div")

        # Select Marital Status
        self.wait_and_click(
            "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[3]/div/div[2]/div/div[2]/div/div/div[2]/i")
        self.wait_and_click(
            "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[3]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/label")

        # Select Male
        self.wait_and_click(
            "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[3]/div[2]/div[2]/div/div[2]/div/div[2]/div/label/span")
        self.wait_and_type(
            "//div[@id='app']/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[3]/div[2]/div/div/div[2]/div/div/input",
            "1994-2-14")
        self.wait_and_click("css:.oxd-form")


if __name__ == "__main__":
    unittest.main(verbosity=2)
