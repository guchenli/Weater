# -*- coding: utf-8 -*-
# @author: GuChenLi
# @time: 2022-10-13
import os
import time

import allure
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from Common import Log, contant
from Common.shell import Shell
from config.dir_config import screenshot_dir

log = Log.MyLog()


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, MobileBy, locator):
        return self.driver.find_element(MobileBy, locator)

    def finds(self, MobileBy, locator):
        return self.driver.find_elements(MobileBy, locator)

    # 滑动到某个元素
    def moveto_text(self, text):
        return self.find(MobileBy.ANDROID_UIAUTOMATOR,
                         'new UiScrollable(new UiSelector().'
                         'scrollable(true).instance(0)).'
                         'scrollIntoView(new UiSelector().'
                         f'text("{text}").instance(0));')

    # 找兄弟元素,例：通过姓名匹配到必填的输入框,,用(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()
    def bro_select(self, text1, text2):
        # father_el = self.find(MobileBy.XPATH, f"//*[@text='{text1}']/..").get_attribute("resource-id")
        father_el = self.find(MobileBy.XPATH, f"//*[contains(@text,'{text1}')]/..").get_attribute("resource-id")
        return self.find(MobileBy.ANDROID_UIAUTOMATOR,
                         f'new UiSelector().resourceId("{father_el}").\
                             childSelector(text("{text2}"))')

    # 显示等待ID出现
    def wait_id_exist(self, ID, timeout=10):
        element: WebDriver = WebDriverWait(self.driver, timeout).until \
            (lambda x: x.find_element_by_id(ID))
        return element

    # 显示等待ID消失
    def wait_id_gone(self, ID, timeout=10):
        element: WebDriver = WebDriverWait(self.driver, timeout).until_not \
            (lambda x: x.find_element_by_id(ID))
        return element

    # 断言toast提示
    def assert_toast_text(self, text):
        toast_info = self.find(MobileBy.XPATH, f"//*[@class='{contant.class_toast}']").text
        assert toast_info == text

    # 进入天气后添加n个城市
    # def start_with_city(self, n):
    #     self.find(MobileBy.ID, contant.id_agree_btn_china).click()
    #     self.find(MobileBy.ID, contant.id_permission_allow_always_button).click()
    #     for i in range(n):
    #         self.wait_refresh()
    #         self.driver.find_element_by_id(contant.id_header_more).click()
    #         self.driver.find_element_by_xpath(f"//*[@text='{contant.manage_cities}']").click()
    #         self.driver.find_element_by_xpath(f"//*[@text='{contant.add_city}']").click()
    #         # time.sleep(1)
    #         # self.driver.find_element_by_id(contant.id_search_src_text).click()
    #         WebDriverWait(self.driver, 10).until(
    #             expected_conditions.element_to_be_clickable((MobileBy.ID, contant.id_search_src_text))).click()
    #         self.driver.find_element_by_id(contant.id_search_src_text).send_keys(get_data()[i])
    #         self.driver.find_element_by_id(contant.id_addcity_item_textview).click()

    # 按下home键

    def go_home(self):
        self.driver.press_keycode(3)
        return self

    # 后台
    def backstage(self):
        self.driver.press_keycode(82)
        return self

    # 上下左右滑动
    def swipe(self, direction):
        window_size = self.driver.get_window_size()
        width = window_size["width"]
        height = window_size["height"]
        if direction == "up":
            self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.2)
        elif direction == "down":
            self.driver.swipe(width * 0.5, height * 0.2, width * 0.5, height * 0.8)
        elif direction == "left":
            self.driver.swipe(width * 0.2, height * 0.5, width * 0.8, height * 0.5)
        elif direction == "right":
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.2, height * 0.5)
        time.sleep(1)
        return self

    # 截图 在allure报告中
    def screen_out(self, pictureName):
        picturePath = os.path.join(screenshot_dir, pictureName + '.png')
        print(picturePath)
        try:
            self.driver.get_screenshot_as_file(picturePath)
            allure.attach.file(picturePath, name=pictureName, attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print(e)
        return self

    # 设置语言
    def set_language(self, language):
        cmd = "adb shell am start -a android.settings.LOCALE_SETTINGS"
        Shell.shell(cmd)
        # time.sleep(3)
        # print(self.driver.page_source)
        self.driver.find_element_by_xpath(f"//*[@text='{language}']").click()
        return self

    def get_mysql(self, table, value):
        pass
        # '''连接数据库'''
        # # 打开数据库连接
        # db = pymysql.connect(host='', port=, db=, user='', passwd='', charset='utf8')
        # # 使用 cursor() 方法创建一个游标对象 cursor
        # cursor = db.cursor()
        # try:
        #     # 使用 execute()  方法执行 SQL 查询
        #     cursor.execute(value)
        #     db.commit()
        # except Exception as e:
        #     print(e)
        #     db.rollback()
        # # 使用 fetchone() 方法获取单条数据.
        # data = cursor.fetchone()
        # # 关闭数据库连接
        # db.close()
        # return data




