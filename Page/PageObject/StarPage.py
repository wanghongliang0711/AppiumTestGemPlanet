# -*- coding: utf-8 -*-
# @Time    : 2020/4/8 12:55
# @File    : StarPage.py
from Page.BasePage import BasePage
from config.ElementConfig import StarPageElements


class StarPage(BasePage):
    """启动默认页，星球"""
    def click_news(self):
        return self.click(*StarPageElements.news)



