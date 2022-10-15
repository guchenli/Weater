# -*- coding: utf-8 -*-
# @author: GuChenLi
# @time: 2022-10-14
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Common import contant
from Common.BasePage import BasePage



class AddCityPage(BasePage):
    def add_suggested_city(self):
        from Page.HomePage import HomePage
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((MobileBy.ID, contant.id_search_src_text)))
        self.find(By.XPATH, "//*[@text='北京']").click()
        return HomePage(self.driver)

    def add_search_city(self, city):
        from Page.HomePage import HomePage
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((MobileBy.ID, contant.id_search_src_text))).click()
        self.driver.find_element_by_id(contant.id_search_src_text).send_keys(city)
        self.driver.find_element_by_id(contant.id_addcity_item_textview).click()
        return HomePage(self.driver)