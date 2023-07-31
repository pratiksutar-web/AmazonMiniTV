import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utilities import ReadConfigurations


@pytest.fixture()
def setup_and_teardown(request):
    browser = ReadConfigurations.read_configurations("basic info", "browser")
    global driver
    if browser.__eq__("chrome"):
        # path = "C:\Selenium With Python\Browsers\chromedriver.exe"
        # serv_obj = Service(path)

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach",True)
        driver = webdriver.Chrome(options=options)
        driver.set_page_load_timeout(15)

    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()

    elif browser.__eq__("edge"):
        driver = webdriver.Edge()

    else:
        print("Please provide a valid browser name from this list chrome/firefox/edge")

    driver.maximize_window()
    app_url = ReadConfigurations.read_configurations("basic info","url")
    driver.get(app_url)
    driver.implicitly_wait(4)
    request.cls.driver = driver
    yield
    driver.quit()
