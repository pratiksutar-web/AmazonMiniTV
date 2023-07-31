
class GetSeriesDetails:
    expected_season1_ep1_name = "E1 | Gareebi Aur Mohabbat"
    expected_season2_ep1_name = "E1 | Batana Sahi Sahi"
    expected_season3_ep1_name = "E1 | Mere Muh Se Nikal Gayi"



    def get_web_series_name(self,season_no,episode_no):

        if season_no.__eq__(1) and episode_no.__eq__(1):
            return self.expected_season1_ep1_name
        elif season_no.__eq__(2) and episode_no.__eq__(1):
            return self.expected_season2_ep1_name
        elif season_no.__eq__(3) and episode_no.__eq__(1):
            return self.expected_season3_ep1_name
