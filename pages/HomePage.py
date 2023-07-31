import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.actions = ActionChains(self.driver)

    popular_web_series_category_xpath_locator = "//h2[text()='Popular Web Series']"
    popular_web_series_category_right_arrow_button_xpath_locator_ = "(//div[@class='CarouselArrows_carouselArrow__7QO0l CarouselArrows_carouselRight__eorpZ'])[4]"
    farzi_mushaira_web_series_xpath_locator = "//img[@alt='Farzi Mushaira - Season 2 - Watch Free']"

    def wait_for_home_page_to_load(self):

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//h2[text()='Popular Web Series']"))).click()

    def scroll_to_popular_web_series(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.popular_web_series_category_xpath_locator)))
        popular_web_series = self.driver.find_element(By.XPATH,self.popular_web_series_category_xpath_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();",popular_web_series)
        time.sleep(4)

    def click_on_popular_web_series_right_arrow_button(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.popular_web_series_category_right_arrow_button_xpath_locator_)))
        self.driver.find_element(By.XPATH,self.popular_web_series_category_right_arrow_button_xpath_locator_).click()
        time.sleep(3)

    def click_on_farzi_mushaira_web_series(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.farzi_mushaira_web_series_xpath_locator)))
        farzi_mushaira = self.driver.find_element(By.XPATH,self.farzi_mushaira_web_series_xpath_locator)
        self.actions.move_to_element(farzi_mushaira).perform()
        time.sleep(2)

        # self.driver.execute_script("arguments[0].scrollIntoView();", farzi_mushaira)
        farzi_mushaira.click()
        time.sleep(2)
