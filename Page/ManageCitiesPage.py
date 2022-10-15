# -*- coding: utf-8 -*-
# @author: GuChenLi
# @time: 2022-10-14
# @File: ManageCitiesPage.py
from Common import contant
from Common.BasePage import BasePage
from Page.AddCityPage import AddCityPage


class ManageCitiesPage(BasePage):
    def click_add_city(self):
        self.driver.find_element_by_xpath(f"//*[@text='{contant.add_city}']").click()
        return AddCityPage(self.driver)