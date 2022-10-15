# -*- coding: utf-8 -*-
# @author: GuChenLi
# @time: 2022-10-13
# @File: WelcomePage.py

import time
from appium.webdriver.common.mobileby import MobileBy
from Common import contant
from Common.BasePage import BasePage
from Page.AddCityPage import AddCityPage
from Page.HomePage import HomePage
from Page.BasicServicesPage import BasicServicesPage


class WelcomePage(BasePage):
    # 点击确认
    def click_agree(self, permission_type):
        self.find(MobileBy.ID, contant.id_agree_btn_china).click()
        if permission_type == 1 :
            self.find(MobileBy.ID, contant.id_permission_allow_always_button).click()
            return HomePage(self.driver)
        if permission_type == 2:
            self.find(MobileBy.ID, contant.id_permission_allow_foreground_only_button).click()
            return HomePage(self.driver)
        if permission_type == 3:
            # self.find(By.ID, contant.id_permission_deny_button).click()
            self.driver.find_element_by_id(contant.id_permission_deny_button).click()
            return AddCityPage(self.driver)

    # 点击确认
    def click_cancel(self):
        self.find(MobileBy.ID, contant.id_disagree_btn_china).click()
        return BasicServicesPage(self.driver)

