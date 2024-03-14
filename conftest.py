import pytest
from selenium import webdriver
from utilities.test_data import TestData

@pytest.fixture(params=["chrome", "firefox", "edge"])
def initialize_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "edge":
        driver = webdriver.Edge()
    request.cls.driver = driver
    print("Browser: ", request.param)
    driver.get(TestData.url)
    driver.maximize_window()
    yield
    print("Close Driver")
    driver.close()

# 1st Step: Declare Variables For Setting Up LambdaTest
user_name = "atipjaitham"
access_token = "8hEEGsAkwBki5bpEzFKV01GsswQF3FLljeawu63St4Sf35EQfM"
remote_url = f"https://{user_name}:{access_token}@hub.lambdatest.com/wd/hub"

# 2nd Step: Define The Desired Capabilities (3 Caps)
chrome_caps = {
    "build": "1.0",
    "name": "LambdaTest Grid On Chrome",
    "platform": "Windows 10",
    "browserName": "Chrome",
    "version": "latest"
}

firefox_caps = {
    "build": "2.0",
    "name": "LambdaTest Grid On Firefox",
    "platform": "Windows 10",
    "browserName": "Firefox",
    "version": "latest"
}

edge_caps = {
    "build": "3.0",
    "name": "LambdaTest Grid On Edge",
    "platform": "Windows 10",
    "browserName": "Edge",
    "version": "latest"
}

# 3rd Step: Connect To LambdaTest Using A Fixture
@pytest.fixture(params=["chrome", "firefox", "edge"])
def driver_initialization(request):
    options = None
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
    elif request.param == "firefox":
        options = webdriver.FirefoxOptions()
    elif request.param == "edge":
        options = webdriver.EdgeOptions()
    driver = webdriver.Remote(command_executor=remote_url, options=options)
    request.cls.driver = driver
    yield
    driver.close()
