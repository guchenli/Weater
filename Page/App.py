# -*- coding: utf-8 -*-
# @author: GuChenLi
# @time: 2022-10-14
import time

from appium import webdriver
from Common import contant
from Common.BasePage import BasePage
from Common.get_data import get_data
from Page.WelcomePage import WelcomePage
from Page.HomePage import HomePage


class App(BasePage):
    # @property
    def start(self):
        if self.driver is None:
            caps = {}
            # 手机 系统信息
            caps['platformName'] = 'Android'
            caps['platformVersion'] = '10'
            # 设备号
            caps['deviceName'] = '9YEDU18924008323'
            # 包名
            caps['appPackage'] = contant.package_weather
            # 启动名
            caps['appActivity'] = contant.activity_home
            caps['automationName'] = 'Uiautomator2'
            # 允许输入中文
            caps['unicodeKeyboard'] = True
            caps['resetKeyboard'] = True
            # app权限 是否重置（清缓存）
            # caps['autoGrantPermissions'] = True
            caps['noReset'] = False
            # 配置chromedriver地址
            # "chromedriverExecutable":

            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(5)
        else:
            # 根据caps内设置信息启动APP
            self.driver.launch_app()
        return self

    def stop(self):
        time.sleep(1)
        self.driver.quit()

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def goto_welcome(self):
        return WelcomePage(self.driver)

    # 添加n个城市
    def start_with_city(self, n):
        self.goto_welcome().click_agree(1).wait_refresh()
        for i in range(n):
            HomePage(self.driver).\
                click_header_more(contant.manage_cities).\
                click_add_city().\
                add_search_city(get_data()[i])
        return HomePage(self.driver)
            # self.driver.find_element_by_id(contant.id_header_more).click()
            # self.driver.find_element_by_xpath(f"//*[@text='{contant.manage_cities}']").click()
            # self.driver.find_element_by_xpath(f"//*[@text='{contant.add_city}']").click()
            # # time.sleep(1)
            # # self.driver.find_element_by_id(contant.id_search_src_text).click()
            # WebDriverWait(self.driver, 10).until(
            #     expected_conditions.element_to_be_clickable((MobileBy.ID, contant.id_search_src_text))).click()
            # self.driver.find_element_by_id(contant.id_search_src_text).send_keys(get_data()[i])
            # self.driver.find_element_by_id(contant.id_addcity_item_textview).click()

    # 找到天气图标
    def find_weather_icon(self):
        self.go_home()
        self.swipe("down")

