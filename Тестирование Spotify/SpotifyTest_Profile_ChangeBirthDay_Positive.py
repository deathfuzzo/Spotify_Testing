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
    driver.find_element_by_link_text("Вход в аккаунт").click()
    driver.find_element_by_id("login-username").send_keys("try.e-mail_4321@gmail.com")
    driver.find_element_by_id("login-password").send_keys("password123")
    driver.find_element_by_id("login-button").click() #вход в тестовый аккаунт
    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#profile > .Menu__menuLink--3F9Kb")))
    driver.find_element_by_css_selector("#profile > .Menu__menuLink--3F9Kb").click() #переход в вкладку "Изменение профиля"
    driver.find_element_by_id("dob-date").click()
    driver.find_element_by_id("dob-date").send_keys("\b")
    driver.find_element_by_id("dob-date").click()
    driver.find_element_by_id("dob-date").send_keys("\b") #очищение поля "День"
    driver.find_element_by_id("dob-date").click()
    driver.find_element_by_id("dob-date").send_keys("9") #посыл тестовых значений в поле "День"
    driver.find_element_by_id("dob-date").click()
    driver.execute_script("window.scrollTo(0,707)")
    driver.find_element_by_css_selector(".Button-sc-8cs45s-0").click() #нажатие на кнопку "Сохранить данные профиля"

