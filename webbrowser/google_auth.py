import time

from selenium.webdriver.common.by import By

from functions.driver_actions import timer, sender, clicker


def google_auth(driver, email, password, reserve):
    """Logining in google account"""
    driver.get(r'https://accounts.google.com/signin/v2/identifier?continue=' + \
               'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1' + \
               '&flowName=GlifWebSignIn&flowEntry = ServiceLogin')

    timer(sender, driver, '//*[@id ="identifierId"]', email)

    timer(clicker, driver, '//*[@id ="identifierNext"]')
    try:
        timer(driver.find_element, By.XPATH, "//span[normalize-space()='Create account']")
    except:
        pass
    timer(sender, driver, '//*[@id ="password"]/div[1]/div / div[1]/input', password)
    timer(clicker, driver, '//*[@id ="passwordNext"]')

    """Здесь запихнуть проверку на 3 сегмент"""

    try:
        time.sleep(3)
        driver.find_element(By.XPATH, "(//ul[@class='OVnw0d'])[1]")
        timer(clicker, driver, "(//div[contains(@role,'link')])[4]")
        timer(sender, driver, "//input[@id='knowledge-preregistered-email-response']", reserve)
        timer(clicker, driver, "(//button[contains(@class,'VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-"
                               "LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b')])[1]")
        timer(driver.find_element, By.XPATH, " //div[@class='WARaV']")
    except:
        try:
            driver.find_element(By.XPATH, " //div[@class='WARaV']")
        except:
            driver.find_element(By.CSS_SELECTOR, ".T-I.T-I-KE.L3")
