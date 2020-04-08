# -*- coding: utf-8 -*-
# @Time    : 2020/4/7 18:51
# @File    : test_SeeNews.py
import time


class TestSeeNews(object):

    def test_see_news(self, ini_page):
        start_page = ini_page[1]
        planet_headlines = ini_page[2]
        for i in range(30):
            print(f"Info: The {i} times")
            start_page.click_news()
            planet_headlines.select_first_news()
            planet_headlines.loop_see_news()
        time.sleep(1)
