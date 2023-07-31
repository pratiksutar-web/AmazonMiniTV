import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from utilities.GetSeriesDetails import GetSeriesDetails


class WebSeriesDetailPage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.actions = ActionChains(self.driver)

    web_series_seasons_list_element_xpath_locator = "//div[@class='rmc-tabs-tab-bar-content']/div"
    web_series_season_one_tab_xpath_locator = "//h2[text()='Season  1']"
    web_series_season_two_tab_xpath_locator = "//h2[text()='Season  2']"
    web_series_season_three_tab_xpath_locator = "//h2[text()='Season  3']"


    farzi_mushaira_season_one_name_xpath_locator = "(//div[text()='E1 | Gareebi Aur Mohabbat'])[2]"
    farzi_mushaira_season_two_name_xpath_locator = "(//div[text()='E1 | Batana Sahi Sahi'])[2]"
    farzi_mushaira_season_three_name_xpath_locator = "(//div[text()='E1 | Mere Muh Se Nikal Gayi'])[2]"

    season_one_ep_one_thumbnail_xpath_locator = "//img[@alt='Gareebi Aur Mohabbat - Watch Free']"
    season_two_ep_one_thumbnail_xpath_locator = "//img[@alt='Batana Sahi Sahi - Watch Free']"
    season_three_ep_one_thumbnail_xpath_locator = "//img[@alt='Mere Muh Se Nikal Gayi - Watch Free']"

    def get_no_of_seasons(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH,self.web_series_seasons_list_element_xpath_locator)))
        web_series_seasons_list = self.driver.find_elements(By.XPATH,self.web_series_seasons_list_element_xpath_locator)
        web_series_no_of_seasons = len(web_series_seasons_list)
        return web_series_no_of_seasons

    def click_on_season_option(self,season_no):
        if season_no.__eq__(1):
            self.wait.until(EC.element_to_be_clickable((By.XPATH,self.web_series_season_one_tab_xpath_locator)))
            self.driver.find_element(By.XPATH,self.web_series_season_one_tab_xpath_locator).click()
        elif season_no.__eq__(2):
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.web_series_season_two_tab_xpath_locator)))
            self.driver.find_element(By.XPATH,self.web_series_season_two_tab_xpath_locator).click()
        elif season_no.__eq__(3):
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.web_series_season_three_tab_xpath_locator)))
            self.driver.find_element(By.XPATH,self.web_series_season_three_tab_xpath_locator).click()


    def get_season_title(self,season_no):
        if season_no.__eq__(1):
            self.wait.until(EC.presence_of_element_located((By.XPATH,self.farzi_mushaira_season_one_name_xpath_locator)))
            season_one_title = self.driver.find_element(By.XPATH,self.farzi_mushaira_season_one_name_xpath_locator).text
            return season_one_title
        elif season_no.__eq__(2):
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.farzi_mushaira_season_two_name_xpath_locator)))
            season_two_title = self.driver.find_element(By.XPATH,self.farzi_mushaira_season_two_name_xpath_locator).text
            return season_two_title
        elif season_no.__eq__(3):
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.farzi_mushaira_season_three_name_xpath_locator)))
            season_three_title = self.driver.find_element(By.XPATH,self.farzi_mushaira_season_three_name_xpath_locator).text
            return season_three_title

    def play_episode_from_season(self,season_no,episode_no,video_duration):

        if season_no.__eq__(1) and episode_no.__eq__(1):
            self.play_episodes_from_season_one(episode_no,video_duration)

        elif season_no.__eq__(2) and episode_no.__eq__(1):
            self.play_episodes_from_season_two(episode_no,video_duration)

        elif season_no.__eq__(3) and episode_no.__eq__(1):
            self.play_episodes_from_season_three(episode_no,video_duration)


    def play_episodes_from_season_one(self,episode_no,video_duration):
        if episode_no.__eq__(1):
            self.wait.until(EC.element_to_be_clickable((By.XPATH,self.season_one_ep_one_thumbnail_xpath_locator)))
            thumbnail_video_element = self.driver.find_element(By.XPATH,self.season_one_ep_one_thumbnail_xpath_locator)
            self.actions.click(thumbnail_video_element).perform()
            time.sleep(video_duration)

    def play_episodes_from_season_two(self,episode_no,video_duration):
        if episode_no.__eq__(1):
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.season_two_ep_one_thumbnail_xpath_locator)))
            thumbnail_video_element = self.driver.find_element(By.XPATH, self.season_two_ep_one_thumbnail_xpath_locator)
            self.actions.click(thumbnail_video_element).perform()
            time.sleep(video_duration)

    def play_episodes_from_season_three(self,episode_no,video_duration):
        if episode_no.__eq__(1):
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.season_three_ep_one_thumbnail_xpath_locator)))
            thumbnail_video_element = self.driver.find_element(By.XPATH, self.season_three_ep_one_thumbnail_xpath_locator)
            self.actions.click(thumbnail_video_element).perform()
            time.sleep(video_duration)

