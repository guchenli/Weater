# -*- coding: utf-8 -*-
# @author: GuChenLi
# @time: 2022-10-13
# @File: test_home.py

import allure
import pytest
from Common import contant
from Page.App import App

class TestHome:
    def setup(self):
        self.app = App()
        self.driver = self.app.start()

    def teardown(self):
        self.app.stop()

    @pytest.mark.app
    @allure.story("管理城市页")  # 类名
    def test_manage(self):
        self.app.goto_welcome().\
            click_agree(3).\
            add_suggested_city().\
            click_header_more(contant.manage_cities).\
            screen_out(contant.manage_cities)

    @pytest.mark.app
    @allure.story("反馈当前天气")  # 类名
    def test_report(self):
        # self.app.goto_welcome().click_agree(1)
        # time.sleep(3)
        # cmd = "adb shell input swipe 500 500 500 1700 2000"
        # Shell.shell(cmd)
        # print(self.driver.page_source)

        # self.app.start_with_city(4)
        # self.app.goto_welcome().click_agree(1).wait_refresh().swipe("up").swipe("down").swipe("left").swipe("right")

        # self.app.start_with_city(3)
        self.app.goto_welcome(). \
            click_agree(1). \
            click_header_more(contant.report_error). \
            screen_out(contant.report_error)

    @pytest.mark.app
    @allure.story("个性换肤")  # 类名
    def test_theme(self):
        self.app.goto_welcome(). \
            click_agree(3). \
            add_suggested_city(). \
            click_header_more(contant.theme). \
            screen_out(contant.theme)

    @pytest.mark.app
    @allure.story("个性换肤")  # 类名
    def test_language(self):
        self.app.set_language("English")
