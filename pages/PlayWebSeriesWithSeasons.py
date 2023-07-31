import time

from pages.VideoPlayerPage import VideoPlayerPage
from pages.WebSeriesDetailPage import WebSeriesDetailPage
from utilities.GetSeriesDetails import GetSeriesDetails


class PlayWebSeriesWithSeasons:
    def __init__(self,driver):
        self.driver = driver


    def play_episode_of_each_season_and_verify(self,no_of_seasons,video_duration):

        web_series_detail_page = WebSeriesDetailPage(self.driver)

        for i in range(1,no_of_seasons):

            if i.__eq__(1):

                web_series_detail_page.click_on_season_option(i)
                season1_ep1_name = web_series_detail_page.get_season_title(i)

                get_series_details = GetSeriesDetails()

                expected_season1_ep1_name = get_series_details.get_web_series_name(i, 1)

                if season1_ep1_name.__eq__(expected_season1_ep1_name):
                    web_series_detail_page.play_episode_from_season(i, 1,video_duration)

                    video_player_page = VideoPlayerPage(self.driver)
                    video_player_page.take_screen_shot(i,expected_season1_ep1_name)

                    video_player_page.pause_the_video()

                    video_player_page.verify_episode_is_playing(i,expected_season1_ep1_name)
                    video_player_page.verify_episode_played_duration_time(i,expected_season1_ep1_name,video_duration)
                    video_player_page.close_currently_playing_episode()


            elif i.__eq__(2):

                web_series_detail_page.click_on_season_option(i)
                season2_ep1_name = web_series_detail_page.get_season_title(i)

                get_series_details = GetSeriesDetails()
                expected_season2_ep1_name = get_series_details.get_web_series_name(i, 1)

                if season2_ep1_name.__eq__(expected_season2_ep1_name):
                    web_series_detail_page.play_episode_from_season(i, 1,video_duration)

                    video_player_page = VideoPlayerPage(self.driver)

                    video_player_page.take_screen_shot(i,expected_season2_ep1_name)

                    video_player_page.pause_the_video()

                    video_player_page.verify_episode_is_playing(i,expected_season2_ep1_name)
                    video_player_page.verify_episode_played_duration_time(i,expected_season2_ep1_name,video_duration)
                    video_player_page.close_currently_playing_episode()


            elif i.__eq__(3):
                web_series_detail_page.click_on_season_option(i)
                season3_ep1_name = web_series_detail_page.get_season_title(i)

                get_series_details = GetSeriesDetails()
                expected_season3_ep1_name = get_series_details.get_web_series_name(i, 1)

                if season3_ep1_name.__eq__(expected_season3_ep1_name):

                    web_series_detail_page.play_episode_from_season(i, 1,video_duration)

                    video_player_page = VideoPlayerPage(self.driver)
                    video_player_page.take_screen_shot(i,expected_season3_ep1_name)
                    video_player_page.pause_the_video()

                    video_player_page.verify_episode_is_playing(i,expected_season3_ep1_name)
                    video_player_page.verify_episode_played_duration_time(i,expected_season3_ep1_name,video_duration)
                    video_player_page.close_currently_playing_episode()

