import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestPortfolioContactForm(unittest.TestCase):
    def setUp(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get("https://tgadek.bitbucket.io/app/contact/index.html") 

    def tearDown(self):
        self.driver.quit()

    def test_invalid_email_field(self):
        """BUG-05: Brak walidacji nieprawidłowego maila"""
        self.driver.find_element(By.ID, "email").send_keys("testmail.com")  
        self.driver.find_element(By.ID, "message").send_keys("Test message")
        self.driver.find_element(By.ID, "send").click()
        error = self.driver.find_element(By.ID, "emailError").text
        self.assertIn("nieprawidłowy", error.lower())

    def test_empty_message_field(self):
        """BUG-06: Brak walidacji pustej wiadomości"""
        self.driver.find_element(By.ID, "email").send_keys("test@mail.com")
        self.driver.find_element(By.ID, "send").click()
        error = self.driver.find_element(By.ID, "messageError").text
        self.assertIn("brak treści", error.lower())


if __name__ == '__main__':
    unittest.main()
