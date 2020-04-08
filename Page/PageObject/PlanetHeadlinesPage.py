# -*- coding: utf-8 -*-
# @Time    : 2020/4/8 14:42
# @File    : PlanetHeadlinesPage.py
from Page.BasePage import BasePage
from config.ElementConfig import PlanetHeadlinesElements
import time


class PlanetHeadlinesPage(BasePage):
    """星球头条页面，新闻页面"""
    def select_first_news(self):
        time.sleep(4)
        elements = self.find_elements(*PlanetHeadlinesElements.article)
        return elements[2].click()

    def loop_see_news(self):
        for i in range(40):
            if i % 2 == 0:
                time.sleep(2)
                self.swipeUp()
            else:
                time.sleep(2)
                self.swipelower()
        self.click(*PlanetHeadlinesElements.back_button)
        time.sleep(1)
        self.click(*PlanetHeadlinesElements.back_button)
