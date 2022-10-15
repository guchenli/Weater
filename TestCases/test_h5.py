# -*- coding: utf-8 -*-
# @author: guchenli
# @time: 2022-10-14
# @File: test_h5.py

import allure
import pytest
from Common import contant
from Page.App import App


class TestH5:
    def setup(self):
        self.app = App()
        self.driver = self.app.start()

    def teardown(self):
        self.app.stop()

    @pytest.mark.H5
    @allure.story("H5")
    def test_(self):
        self.app.goto_welcome().click_agree(3)
