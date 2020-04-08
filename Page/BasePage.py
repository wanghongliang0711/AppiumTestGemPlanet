# -*- coding: utf-8 -*-
# @Time    : 2020/4/8 10:07
# @File    : BasePage.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    """结合显示等待封装一些selenium内置方法"""
    def __init__(self, driver, timeout=30):
        self.byDic = {
            'id': By.ID,
            'name': By.NAME,
            'class_name': By.CLASS_NAME,
            'xpath': By.XPATH,
            'link_text': By.LINK_TEXT
        }
        self.driver = driver
        self.out_time = timeout

    def find_elements(self, by, locator):
        try:
            print(f'Info:Starting find the elements "{locator}" by "{by}"!')
            elements = WebDriverWait(self.driver, self.out_time).until(
                lambda x: x.find_elements(by, locator))
        except Exception as e:
            print(f'error: found "{locator}" timeout!', e)
        else:
            return elements

    def find_element(self, by, locator):
        """
        find alone element
        :param by: eg: id, name, xpath, css.....
        :param locator: id, name, xpath for str
        :return: element object
        """
        try:
            print(f'Info:Starting find the element "{locator}" by "{by}"!')
            element = WebDriverWait(self.driver, self.out_time).until(
                lambda x: x.find_element(by, locator))
        except Exception as e:
            print(f'error: found "{locator}" timeout!', e)
        else:
            return element

    def load_url(self, url):
        """加载url"""
        print('info: string upload url "{}"'.format(url))
        self.driver.get(url)

    def click(self, by, locator):
        """点击某个元素"""
        try:
            element = self.find_element(by, locator)
            if element.get_attribute("enabled"):
                element.click()
            else:
                print("元素不可以点击")
        except Exception as e:
            print(f'click error: found "{locator}" !', e)

    def clear(self, by, locator):
        """清理数据"""
        print('info:clearing value')
        try:
            element = self.find_element(by, locator)
            element.clear()
        except Exception as e:
            print(f'clear error: found "{locator}" !', e)

    def send_keys(self, by, locator, value=''):
        """写数据"""
        print('info:input "{}"'.format(value))
        try:
            element = self.find_element(by, locator)
            element.send_keys(value)
        except Exception as e:
            print(f'send_keys error: found "{locator}" !', e)

    def get_element_text(self, by, locator, name=None):
        """获取某一个元素的text信息"""
        try:
            element = self.find_element(by, locator)
            if name:
                return element.get_attribute(name)
            else:
                return element.text
        except Exception as e:
            print(f'get_element_text error: found "{locator}" !', e)

    def get_source(self):
        """获取页面源码"""
        return self.driver.page_source

    def swipelower(self, t=600, n=1):
        '''向下滑动'''
        try:
            l = self.driver.get_window_size()
            # print(l)  # {'width': 1532, 'height': 2560}
            x1 = l['width'] * 0.5  # 获取宽度x1
            y1 = l['height'] * 0.3  # 起始值y1
            y2 = l['height'] * 0.95  # 结束值y2
            # print(x1,y1,x2 )
            for i in range(n):
                self.driver.swipe(x1, y1, x1, y2, duration=t)
        except Exception as e:
            # logger.warning("swipeRight." ,e)
            raise Exception("swipelower 失败", e)

    def swipeUp(self, t=600, n=1):
        '''向上滑动'''
        try:
            l = self.driver.get_window_size()
            # print(l)  # {'width': 1532, 'height': 2560}
            x1 = l['width'] * 0.5  # 获取宽度x1
            y1 = l['height'] * 0.95  # 起始值y1
            y2 = l['height'] * 0.3  # 结束值y2
            # print(x1,y1,x2 )
            for i in range(n):
                self.driver.swipe(x1, y1, x1, y2, duration=t)
        except Exception as e:
            # logger.warning("swipeRight." ,e)
            raise Exception("swipeUp 失败", e)
