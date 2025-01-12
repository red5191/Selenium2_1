# Прописываем в терминале:
# python -m pip install --upgrade pip (Обновление менеджера пакетов pip)
# pip install selenium (Устанавливаем библиотеку selenium)
# pip install webdriver-manager (Устанавливаем webdriver-manager)

# импортируем необходимые библиотеки и элементы
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# создаем и настраиваем экземпляр driver класса webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
# options.add_argument('--headless')
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

# создаем переменную содержащую базовую ссылку и открываем её с помощью созданного ранее driver
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

# вводим логин, пароль и имитируем нажатие Enter
user_name = driver.find_element(By.XPATH, "//*[@id='user-name']")
user_name.send_keys('standard_user')
password = driver.find_element(By.NAME , "password")
password.send_keys('secret_sauce', Keys.ENTER)

# записываем в переменные название и цену первого товара и добавляем его в корзину
value_product1 = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']").text
print(f'Product1: {value_product1}')
value_price_product1 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div").text
print(f'Product1 Price: {value_price_product1}')
select_product1 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
select_product1.click()
print('Select product1')

# повторяем то же самое для второго товара
value_product2 = driver.find_element(By.XPATH, "//*[@id='item_0_title_link']/div").text
print(f'Product2: {value_product2}')
value_price_product2 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div").text
print(f'Product2 Price: {value_price_product2}')
select_product2 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")
select_product2.click()
print('Select product2')

# открываем корзину
button_cart_link = driver.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']")
button_cart_link.click()
print('Enter Cart')

# проверяем соответствие наименований и цен в корзине
value_cart_product1 = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']").text
print(f'Cart Product1: {value_cart_product1}')
assert value_product1 == value_cart_product1
print('Cart Info Product 1 GOOD')

value_cart_price_product1 = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div").text
print(f'Cart Product1 Price: {value_cart_price_product1}')
assert value_price_product1 == value_cart_price_product1
print('Cart Price Product 1 GOOD')

value_cart_product2 = driver.find_element(By.XPATH, "//*[@id='item_0_title_link']/div").text
print(f'Cart Product2: {value_cart_product2}')
assert value_product2 == value_cart_product2
print('Cart Info Product 2 GOOD')

value_cart_price_product2 = driver.find_element(By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[4]/div[2]/div[2]/div").text
print(f'Cart Product2 Price: {value_cart_price_product2}')
assert value_price_product2 == value_cart_price_product2
print('Cart Price Product 2 GOOD')

# переходим по кнопке "Checkout", вводим данные заказчика и переходим по кнопке "Continue"
checkout = driver.find_element(By.XPATH, "//*[@id='checkout']")
checkout.click()
print('Click Checkout')
first_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name.send_keys('Tyler')
print('Input First Name')
last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
last_name.send_keys('Durden')
print('Input Last Name')
postal_code = driver.find_element(By.XPATH, "//input[@id='postal-code']")
postal_code.send_keys('123456')
print('Input Postal Code')
button_continue = driver.find_element(By.XPATH, "//input[@id='continue']")
button_continue.click()
print('Click Continue')

# Сверяем наименования и цены на финальной странице оформления заказа
value_final_product1 = driver.find_element(By.XPATH, "//*[@id='item_4_title_link']").text
print(f'Final Product1: {value_final_product1}')
assert value_product1 == value_final_product1
print('Final Info Product 1 GOOD')

value_final_price_product1 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[3]/div[2]/div[2]/div").text
print(f'Final Product1 Price: {value_final_price_product1}')
assert value_price_product1 == value_final_price_product1
print('Final Price Product 1 GOOD')

value_final_product2 = driver.find_element(By.XPATH, "//*[@id='item_0_title_link']/div").text
print(f'Final Product2: {value_cart_product2}')
assert value_product2 == value_final_product2
print('Final Info Product 2 GOOD')

value_final_price_product2 = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[1]/div[4]/div[2]/div[2]/div").text
print(f'Final Product2 Price: {value_final_price_product2}')
assert value_price_product2 == value_final_price_product2
print('Final Price Product 2 GOOD')

value_summary_price = driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[6]").text
print(f'Summary Price: {value_summary_price}')
item_total = "Item total: $" + str(float(value_final_price_product1[1:]) + float(value_final_price_product2[1:]))
print(item_total)
assert value_summary_price == item_total
print('Summary Price GOOD')

# завершаем оформление заказа и удостоверяемся что находимся на нужной странице
button_finish = driver.find_element(By.XPATH, "//*[@id='finish']")
button_finish.click()
print('Click Finish Button')

value_checkout_complete = driver.find_element(By.XPATH, "//*[contains(text(), 'Thank you for your order!')]").text
print(f'Text on page is: {value_checkout_complete}')
assert value_checkout_complete == 'Thank you for your order!'
print('Order completed successfully')

# создаем скриншот результата выполнения кода
# time.sleep(2)
# now_date = datetime.datetime.now().strftime('%Y.%m.%d-%H.%M.%S')
# name_screenshot = 'screenshot' + now_date + '.png'
# driver.save_screenshot('C:\\Users\\the_r\\PycharmProjects\\Selenium2_1\\screenshots\\' + name_screenshot)
