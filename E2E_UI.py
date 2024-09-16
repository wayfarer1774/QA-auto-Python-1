from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from time import sleep

class TestPurchaseFlow(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")

    def test_buy_item(self):
        # 1. Проведем авторизацию
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        username_field.send_keys("standard_user")

        password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        password_field.send_keys("secret_sauce")

        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        )
        login_button.click()

        # 2. Добавим товар в корзину
        add_to_cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        add_to_cart_button.click()

        # 3. Перейдем в корзину
        cart_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'shopping_cart_badge'))
        )
        cart_button.click()

        # 4. Убедимся, что товар добавлен
        item_in_cart = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "item_4_title_link"))
        )
        self.assertTrue(item_in_cart.is_displayed(), "Товар не найден в корзине")

        # 5. Оформим покупку
        checkout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_button.click()

        # 6. Заполним контактные данные
        first_name_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        first_name_field.send_keys("Alexander")

        last_name_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "last-name"))
        )
        last_name_field.send_keys("Ivanov")

        postal_code_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "postal-code"))
        )
        postal_code_field.send_keys("119415")

        continue_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "continue"))
        )
        continue_button.click()

        # 7. Завершим покупку
        finish_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "finish"))
        )
        finish_button.click()

        # 8. Проверим, что покупка произведена
        div_header = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "complete-text"))
        )
        div_header_text = div_header.text
        self.assertEqual(div_header_text, "Your order has been dispatched, and will arrive just as fast as the pony can get there!", "Произошла ошибка. Попробуйте ещё.")

        # 9. Задержка для визуальной проверки завершения сценария (расскомментировать при необходимости)
        #sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()