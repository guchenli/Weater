# -*- coding: utf-8 -*-
# @author: GuChenLi
# @time: 2022-10-13
# @File: HomePage.py
import time

from appium.webdriver.common.mobileby import MobileBy
from Common import contant
from Common.BasePage import BasePage
from Page.ManageCitiesPage import ManageCitiesPage
from Page.WeatherWidgetPage import WeatherWidgetPage
from Page.ReportErrorPage import ReportErrorPage
from Page.ThemePage import ThemePage
from Page.SettingPage import SettingPage


class HomePage(BasePage):
    # 右上角菜单
    def click_header_more(self, text):
        self.driver.find_element_by_id(contant.id_header_more).click()
        # self.find(MobileBy.XPATH, f"//*[@text={text}]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath(f"//*[@text='{text}']").click()
        if text == contant.manage_cities:
            return ManageCitiesPage(self.driver)
        elif text == contant.weather_widget:
            return WeatherWidgetPage(self.driver)
        elif text == contant.report_error:
            return ReportErrorPage(self.driver)
        elif text == contant.theme:
            return ThemePage(self.driver)
        elif text == contant.share:
            return self
        elif text == contant.settings:
            return SettingPage(self.driver)

    # 点击实况天气
    def click_current_weather(self):
        self.driver.find_element_by_xpath(
            f"//*[@resource-id='{contant.id_current_temprature}']").click()
        self.driver.swipe(500, 1800, 500, 300)
        self.driver.find_element_by_xpath("//*[@text='天气地图']").click()

        # 下拉刷新
    def refresh(self):
        while self.find(MobileBy.ID, contant.id_current_temprature) is None:
             self.swipe("down")
        self.swipe("down")
        return self

    # 等待下拉刷新
    def wait_refresh(self):
        self.wait_id_gone(contant.id_head_progressBar)
        return self

