import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestCalculatorCases(unittest.TestCase):
    def setUp(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)

    def tearDown(self):
        self.driver.quit()

    def test_addition_valid_input(self):
        self.driver.get('https://tgadek.bitbucket.io/app/calc/prod/index.html')
        self.driver.find_element(By.ID, "number1").send_keys("2")
        self.driver.find_element(By.ID, "number2").send_keys("4")
        self.driver.find_element(By.CSS_SELECTOR, "input[type='button']").click()
        result = self.driver.find_element(By.ID, "result").text
        self.assertEqual(result, "2 + 4 = 6")

    def test_negative_number_input(self):
        self.driver.get('https://tgadek.bitbucket.io/app/calc/prod/index.html')
        self.driver.find_element(By.ID, "number1").send_keys("4")
        self.driver.find_element(By.ID, "number2").send_keys("-2")
        self.driver.find_element(By.CSS_SELECTOR, "input[type='button']").click()
        result = self.driver.find_element(By.ID, "result").text
        self.assertEqual(result, "4 + -2 = 2") 

    def test_empty_first_field(self):
        self.driver.get('https://tgadek.bitbucket.io/app/calc/prod/index.html')
        self.driver.find_element(By.ID, "number2").send_keys("4")
        self.driver.find_element(By.CSS_SELECTOR, "input[type='button']").click()
        result = self.driver.find_element(By.ID, "result").text
        self.assertTrue("Błędne dane" in result or "NaN" in result) 

    def test_large_values(self):
        self.driver.get('https://tgadek.bitbucket.io/app/calc/prod/index.html')
        self.driver.find_element(By.ID, "number1").send_keys("1e+40")
        self.driver.find_element(By.ID, "number2").send_keys("1e+40")
        self.driver.find_element(By.CSS_SELECTOR, "input[type='button']").click()
        result = self.driver.find_element(By.ID, "result").text
        self.assertTrue("1e+40" in result or "zbyt duża liczba" in result)  

    def test_invalid_email(self):
        self.driver.get('https://tgadek.bitbucket.io/app/contact/index.html')
        self.driver.find_element(By.ID, "email").send_keys("testemail.com")
        self.driver.find_element(By.ID, "message").send_keys("test")
        self.driver.find_element(By.ID, "send").click()
        error = self.driver.find_element(By.ID, "emailError").text
        self.assertIn("nieprawidłowy", error.lower())

    def test_empty_message_field(self):
        self.driver.get('https://tgadek.bitbucket.io/app/contact/index.html')
        self.driver.find_element(By.ID, "email").send_keys("test@mail.com")
        self.driver.find_element(By.ID, "send").click()
        error = self.driver.find_element(By.ID, "messageError").text
        self.assertIn("brak treści", error.lower())


if __name__ == '__main__':
    unittest.main()
