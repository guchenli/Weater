# -*- coding: utf-8 -*-
# @author: guchenli
# @time: 2022-10-14
# @File: test_FA.py

import allure
import pytest
from Common import contant
from Page.App import App


class TestFA:
    def setup(self):
        self.app = App()
        self.driver = self.app.start()

    def teardown(self):
        self.app.stop()

    @pytest.mark.FA
    @allure.story("FA卡片")
    def test_(self):
        self.app.goto_welcome().click_agree(3)
