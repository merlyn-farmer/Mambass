import time

from selenium.webdriver.common.by import By

from functions.driver_actions import timer, clicker, sender
from functions.sms_activate_apis import *


def set_sms_code(driver, country):
    cou = None
    driver.get('https://www.mamba.ru')
    timer(clicker, driver, "//a[@data-name='by-phone-action']")
    
    time.sleep(2)
    elem = driver.find_element(By.CSS_SELECTOR, ".sc-1oc8snq-1.fnAXkI")
    time.sleep(1)
    driver.execute_script("arguments[0].click();", elem)
    timer(clicker, driver, "(//div[@class='sc-1oc8snq-1 fnAXkI'])[1]")
    # gr - +49, eng - +44, aus - +61, Lithuania - +370
    if country == "eng":
        """England"""
        timer(clicker, driver, "(//li[@value='34'])[1]")
        cou = "eng"
    elif country == "aus":
        """Austria"""
        timer(clicker, driver, "(//li[@value='2'])[1]")
        cou = "aus"
    elif country == "ger":
        """Germany"""
        timer(clicker, driver, "(//li[@value='49'])[1]")
        cou = "ger"
    elif country == "lit":
        """Lithuania"""
        timer(clicker, driver, "(//li[@value='103'])[1]")
        cou = "lit"

    country, operator = country_number(cou)
    phone, num_id = five_sim_buy(country, operator)

    timer(sender, driver, "//input[@placeholder='Номер телефона']", phone)

    timer(clicker, driver, "//input[@value='Получить код подтверждения']")
    time.sleep(63)
    timer(clicker, driver, "//button[contains(text(),'Попробовать другой способ')]")

    def set_code():
        sms_code = None
        for _ in range(2):
            time.sleep(30)
            sms_code = five_sim_check(num_id=num_id)
            if sms_code:
                timer(sender, driver, "//input[@placeholder='Код подтверждения']", str(sms_code))
                return True

        if not sms_code:
            return False

    print('set code first')
    sms_code = set_code()

    if not sms_code:
        print('second')
        timer(clicker, driver, "//button[contains(text(),'Попробовать снова')]")
        sms_code = set_code()

    if not sms_code:
        pass

    return sms_code
