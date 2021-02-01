import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    print(wd.capabilities)
    return wd


def test_example(driver):
    driver.get("https://www.spotify.com/")
    driver.find_element_by_css_selector(".mh-menu-closed").click()
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Вход в аккаунт")))
    driver.find_element_by_link_text("Вход в аккаунт").click() #переход на страницу авторизации
    driver.find_element_by_id("login-username").send_keys("try.e-mail_4321@gmail.com") #ввод в поле email
    driver.find_element_by_id("login-password").send_keys("password123") #ввод в поле пароль
    driver.find_element_by_id("login-button").click() #нажатие на кнопку "Войти"

