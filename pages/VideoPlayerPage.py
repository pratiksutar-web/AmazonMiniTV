import time
import logging
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.LogMessageInFile import LogMessageInFile


class VideoPlayerPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.actions = ActionChains(self.driver)

    video_play_button_icon_css_locator = "img[alt='play']"
    video_pause_button_icon_css_locator = "img[alt='pause']"
    video_played_duration_time_css_locator = "div[class=' BottomPanel_videoTimer__sbWcU BottomPanel_landscape__tEqjI']"
    video_close_button_xpath_locator = "//div[@class=' PlayerSkin_container___x4_d PlayerSkin_backgroundColor__doLgQ']/div/div[2]"

    def verify_episode_is_playing(self, season_no, episode_name):

        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,self.video_play_button_icon_css_locator)))
        video_play_button = self.driver.find_element(By.CSS_SELECTOR, self.video_play_button_icon_css_locator)

        try:
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,self.video_pause_button_icon_css_locator)))
            video_pause_button = self.driver.find_element(By.CSS_SELECTOR, self.video_pause_button_icon_css_locator)

        except:

            self.wait.until(EC.visibility_of(video_play_button))

            assert video_play_button.is_displayed()

            if video_play_button.is_displayed():
                message = "Congrats.! " + "S" + str(season_no) + " " + episode_name + " is playing smoothly"
                # print("Congrats.!", episode_name, " is playing smoothly")
                # print(message)

                log_message_in_file = LogMessageInFile()
                log_message_in_file.log_message_into_file(message, "info")


            elif video_pause_button.is_displayed():
                message = "The video is paused. Please click on play button to play the video"
                log_message_in_file = LogMessageInFile()
                log_message_in_file.log_message_into_file(message, "warning")

    def verify_episode_played_duration_time(self, season_no, episode_name,video_duration):

        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,self.video_played_duration_time_css_locator)))
        video_time_duration = self.driver.find_element(By.CSS_SELECTOR,self.video_played_duration_time_css_locator).text

        # print(video_time_duration)
        # Add log here

        video_time_duration_played_list = video_time_duration.split("/")
        video_time_duration_played_in_min_and_sec = video_time_duration_played_list[0]
        video_time_duration_in_min_and_sec_list = video_time_duration_played_in_min_and_sec.split(":")
        video_time_duration_played_in_minutes = video_time_duration_in_min_and_sec_list[0]
        video_time_duration_played_in_seconds = video_time_duration_in_min_and_sec_list[1]

        assert int(video_time_duration_played_in_seconds) >1 and int(video_time_duration_played_in_seconds)<= video_duration

        if int(video_time_duration_played_in_seconds) > 1:
            message = "S" + str(season_no) + " " + episode_name + " played successfully for " + video_time_duration_played_in_minutes + " Minutes and " + video_time_duration_played_in_seconds + " Seconds"
            # print(message)
            log_message_in_file = LogMessageInFile()
            log_message_in_file.log_message_into_file(message, "info")

            # Add log message here

    def close_currently_playing_episode(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.video_close_button_xpath_locator)))
        close_button = self.driver.find_element(By.XPATH, self.video_close_button_xpath_locator)
        self.actions.move_to_element(close_button).perform()
        self.actions.click(close_button).perform()
        message = "The video played successfully and closed"

        log_message_in_file = LogMessageInFile()
        log_message_in_file.log_message_into_file(message, "info")

    def take_screen_shot(self, season_no, episode_name):
        path = "screenshots/" + "S" + str(season_no) + "_" + episode_name + ".png"
        result_path = path.replace(" | ", "_")
        # print(result_path)

        # print(path)
        self.driver.save_screenshot(result_path)

    def pause_the_video(self):
        self.actions.key_down(Keys.SPACE).perform()
        self.actions.key_up(Keys.SPACE).perform()
