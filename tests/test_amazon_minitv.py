import pytest
from pages.HomePage import HomePage
from pages.WebSeriesDetailPage import WebSeriesDetailPage
from pages.PlayWebSeriesWithSeasons import PlayWebSeriesWithSeasons


@pytest.mark.usefixtures("setup_and_teardown")
class TestAmazonMiniTV:
    def test_amazon_video_player(self):
        home_page = HomePage(self.driver)

        home_page.wait_for_home_page_to_load()
        home_page.scroll_to_popular_web_series()
        home_page.click_on_popular_web_series_right_arrow_button()
        home_page.click_on_farzi_mushaira_web_series()

        web_series_detail_page = WebSeriesDetailPage(self.driver)
        no_of_seasons = web_series_detail_page.get_no_of_seasons()
        print(no_of_seasons)

        play_web_series_with_seasons = PlayWebSeriesWithSeasons(self.driver)
        play_web_series_with_seasons.play_episode_of_each_season_and_verify(no_of_seasons,10)

