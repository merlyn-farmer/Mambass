import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from functions.driver_actions import timer, clicker, sender
from functions.sms_activate_apis import five_sim_buy
from webbrowser.sms_activate import set_sms_code

russian_female_names_en = ['Anastasia', 'Maria', 'Daria', 'Yulia', 'Anna', 'Ekaterina', 'Olga', 'Natalia', 'Elena',
                           'Irina', 'Alexandra', 'Polina', 'Ksenia', 'Kristina', 'Vera', 'Tatiana', 'Sofiya', 'Alina',
                           'Arina', 'Svetlana', 'Nadezhda', 'Galina', 'Margarita', 'Yana', 'Taisiya', 'Lyudmila',
                           'Zoya',
                           'Valentina', 'Elizaveta', 'Ulyana', 'Lidiya', 'Viktoriya', 'Yaroslava', 'Yekaterina',
                           'Mariya',
                           'Yelena', 'Zinaida', 'Raisa', 'Marina', 'Tamara', 'Margarita', 'Inna', 'Alla', 'Sofiya',
                           'Anastasiya', 'Evgeniya', 'Ekaterina', 'Lyubov', 'Irina', 'Angelina', 'Lyudmila', 'Nina',
                           'Alena', 'Tatyana', 'Natalya', 'Anna', 'Kristina', 'Svetlana', 'Darya', 'Sofia', 'Valeriya',
                           'Valentina', 'Kira', 'Marianna', 'Galina', 'Veronika', 'Roza', 'Lubov', 'Anastasia',
                           'Margarita',
                           'Diana', 'Katya', 'Aurora', 'Yuliya', 'Olga', 'Sofiya', 'Inna', 'Natalia', 'Svetlana',
                           'Angelina',
                           'Irina', 'Taisiya', 'Anna', 'Yana', 'Elizaveta', 'Polina', 'Kseniya', 'Aleksandra', 'Olivia',
                           'Mariya', 'Eva', 'Sara', 'Lidiya', 'Alina', 'Raisa', 'Victoria', 'Kira', 'Yekaterina',
                           'Alienor']
russian_female_names_ru = ['Александра', 'Алена', 'Алина', 'Алиса', 'Алла', 'Анастасия', 'Ангелина', 'Анна', 'Арина',
                           'Валентина', 'Валерия', 'Варвара', 'Вера', 'Вероника', 'Виктория', 'Галина', 'Дарья', 'Ева',
                           'Евгения', 'Екатерина', 'Елена', 'Елизавета', 'Жанна', 'Злата', 'Инна', 'Ирина', 'Карина',
                           'Кира', 'Кристина', 'Ксения', 'Лариса', 'Лидия', 'Любовь', 'Людмила', 'Маргарита', 'Марина',
                           'Мария', 'Мила', 'Милана', 'Милена', 'Надежда', 'Наталья', 'Нина', 'Оксана', 'Олеся',
                           'Ольга', 'Полина', 'Раиса', 'Светлана', 'София', 'Тамара', 'Татьяна', 'Ульяна', 'Юлия',
                           'Яна', 'Ярослава', 'Агата', 'Агнесса', 'Алевтина', 'Алима', 'Алла', 'Альбина', 'Амалия',
                           'Анисья', 'Ариадна', 'Валентина', 'Валерия', 'Василиса', 'Вера', 'Вероника', 'Влада',
                           'Владислава', 'Галина', 'Дарина', 'Диана', 'Дина', 'Евгения', 'Екатерина', 'Елена',
                           'Елизавета', 'Жанна', 'Зарина', 'Зоя', 'Инга', 'Инесса', 'Ия', 'Камилла', 'Каролина',
                           'Кира', 'Клавдия', 'Кристина', 'Леся', 'Майя', 'Маргарита', 'Марина', 'Мирослава',
                           'Надежда', 'Наталья', 'Оксана', 'Ольга', 'Полина', 'Роза']


def mamba_login(driver, email):
    driver.get("https://mamba.ru")

    timer(clicker, driver, "(//button[contains(text(),'Женщина')])[1]")
    timer(clicker, driver, "//button[contains(text(),'С мужчинами')]")
    timer(clicker, driver, "//button[contains(text(),'Встреча, свидание')]")
    timer(clicker, driver, "//button[contains(text(),'Любого')]")
    timer(clicker, driver, "//button[contains(text(),'Любого')]")
    timer(sender, driver, "//input[@placeholder='Ваше имя']", "Вика")
    timer(clicker, driver, "//input[@value='Далее']")

    day_box = driver.find_element(By.XPATH, "//select[@name='day']")
    select = Select(day_box)

    select.select_by_visible_text("1")
    time.sleep(2)
    month_box = driver.find_element(By.XPATH, "//select[@name='month']")
    time.sleep(0.5)
    select = Select(month_box)
    time.sleep(0.5)
    select.select_by_visible_text("январь")
    time.sleep(0.5)
    year_box = driver.find_element(By.XPATH, "//select[@name='year']")
    time.sleep(0.5)
    select = Select(year_box)
    time.sleep(0.5)
    select.select_by_visible_text("2000")

    timer(clicker, driver, "//input[@value='Далее']")
    timer(sender, driver, "//input[@placeholder='Электронная почта']", email)
    timer(clicker, driver, "//button[contains(text(),'Регистрация с почтой')]")



def send_code(driver):

    res = set_sms_code(driver, 'ger')

    if not res:
        res = set_sms_code(driver, 'eng')

    if not res:
        raise Exception('sms-code no coming')

    time.sleep(10)
    print('clc понятно')
    timer(clicker, driver, "//button[contains(text(),'Понятно')]")
