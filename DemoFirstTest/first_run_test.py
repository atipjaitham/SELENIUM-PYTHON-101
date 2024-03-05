import time
from selenium import webdriver

def test_lambdatest_playground():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.lambdatest.com/selenium-playground/")
    print("Title: ", driver.title)

def test2_lambdatest_ecommerce():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://ecommerce-playground.lambdatest.io/")
    print("Title: ", driver.title)

def testWebSite():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://atipjaitham.github.io/")
    print("Title: ", driver.title)