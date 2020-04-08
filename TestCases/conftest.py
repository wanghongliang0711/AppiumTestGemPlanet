# -*- coding: utf-8 -*-
# @Time    : 2020/4/7 18:50
# @File    : conftest.py
from Page.PageObject.PlanetHeadlinesPage import PlanetHeadlinesPage
from Page.PageObject.StarPage import StarPage
import pytest


@pytest.fixture(scope='class')
def ini_page(driver):
    start_page = StarPage(driver)
    planet_headlines = PlanetHeadlinesPage(driver)
    print("********ini_pages(driver)********")
    yield driver, start_page, planet_headlines
