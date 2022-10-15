# -*- coding: utf-8 -*-
# @author: GuChenLi
# @time: 2022-10-13

import time

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.extensions.android.gsm import GsmCallActions
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Common import contant
from Common.get_data import get_data


class TestDemo:
    def setup(self):
        desire_cap = {
            "platformName": "android",  # 安卓
            "platformVersion": "10.0",  # 版本
            "deviceName": "9YEDU18924008323",  # 设备
            "appPackage": "com.huawei.android.totemweather",
            "appActivity": ".WeatherHome",
            "noReset": True,  # 是否重置APP，即清缓存
            "unicodeKeyboard": True,  # 这两个设置 send_keys()传入中文时需要配置,设置之后会有Appium的输入法守护来执行输入操作
            "resetKeyboard": True,
            # "dontStopAppOnReset": True  #不终止当前APP上的内容,调试时使用
            "chromedriverExecutable":"D:/chromedriver/chromedriver.exe",
            "chromedriverExecutableDir":"D:/chromedriver/"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(5)

    def teardown(self):
        time.sleep(3)
        # self.driver.quit()

    # @pytest.mark.parametrize('text', ["北京", "上海", "广州"])
    @pytest.mark.parametrize('text', get_data())
    def test_1(self, text):
        self.driver.find_element_by_accessibility_id("更多选项").click()
        self.driver.find_element_by_xpath("//*[@text='管理城市']").click()
        self.driver.find_element_by_xpath("//*[@text='添加城市']").click()
        time.sleep(1)
        el = self.driver.find_element_by_id(contant.id_search_src_text)
        print(el.text)
        print(el.location)
        print(el.size)
        el.click()
        self.driver.find_element_by_id("com.huawei.android.totemweather:id/search_src_text").send_keys(text)

    # 触屏操作 press按下 release松开 wait等待 long_press长按 tap点击 move_to滑动 perform执行
    def test_touchaction(self):
        rect = self.driver.get_window_rect()
        print(rect)
        width = rect["width"]
        height = rect["height"]
        action = TouchAction(self.driver)
        action.press(x=0.5 * width, y=0.9 * height).wait(500).move_to(x=0.5 * width, y=0.2 * height).release().perform()
        action.press(x=500, y=1800).wait(500).move_to(x=500, y=200).release().perform()

        # 多指
        def test_duozhi(self):
            # self.driver.back()
            self.driver.press_keycode(3)  # 手机按键
            time.sleep(3)
            window_size = self.driver.get_window_size()  # 获取整个屏幕的大小尺寸
            print(window_size)  # {'width': 1080, 'height': 2232}
            #  获取 中心位置
            width = window_size["width"]
            height = window_size["height"]
            action1 = TouchAction(self.driver)  # 事件一定要区分成两个对象
            action2 = TouchAction(self.driver)  # 事件一定要区分成两个对象
            # 缩放手势
            action1.press(x=width * 0.8, y=height * 0.2).wait(100).move_to(x=width * 0.6, y=height * 0.4).release()
            action2.press(x=width * 0.2, y=height * 0.8).wait(100).move_to(x=width * 0.4, y=height * 0.6).release()

            multi_action = MultiAction(self.driver)
            multi_action.add(action1)
            multi_action.add(action2)
            multi_action.perform()

    # XPATH定位  父子节点 //下子子孙孙  /下子
    def test_xpath(self):
        self.driver.find_element_by_xpath("//*[@content-desc='更多选项']").click()
        # 点击天气设置
        el = self.driver.find_element_by_xpath("//*[@text='分享']/../../..//android.widget.LinearLayout[6]")
        el.click()

    # uiautomator 定位
    def test_ui(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().description("更多选项")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("管理城市")').click()
        self.driver.find_element_by_android_uiautomator \
                (
                'new UiSelector().text("添加城市").resourceId("com.huawei.android.totemweather:id/mng_city_bottom_tv")').click()

        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).'
            'scrollIntoView(new UiSelector().text("北京·故宫").instance(0));').click()

    # 等待
    def test_time(self):
        self.driver.find_element_by_accessibility_id("更多选项").click()
        self.driver.find_element_by_xpath("//*[@text='管理城市']").click()
        self.driver.find_element_by_xpath("//*[@text='添加城市']").click()
        """
        selenium.common.exceptions.StaleElementReferenceException: Message: 
        The element 'By.id: com.huawei.android.totemweather:id/search_src_text' does not exist in DOM anymore
        """
        # el = self.driver.find_element_by_id("com.huawei.android.totemweather:id/search_src_text")
        # el.click()
        lc = (MobileBy.ID, "com.huawei.android.totemweather:id/search_src_text")
        el = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(lc))
        # el = WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*lc))
        # self.driver.find_element(*lc).click()
        el.click()
        print(el.text)

    # toast提示
    def test_toast(self):
        self.driver.find_element_by_accessibility_id("更多选项").click()
        self.driver.find_element_by_xpath("//*[@text='反馈当前天气']").click()
        self.driver.find_element_by_xpath("//*[@text='晴']").click()
        self.driver.find_element_by_xpath("//*[@text='提交']").click()
        print(self.driver.page_source)
        print(self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text)
        self.driver.quit()

    def test_web(self):
        print("跳转前", self.driver.contexts)
        # print(self.driver.page_source)
        self.driver.find_element_by_xpath("//*[@resource-id='com.huawei.android.totemweather:id/current_temprature']").click()
        time.sleep(2)
        print("跳转后", self.driver.contexts)
        # print(self.driver.page_source)
        # self.driver.switch_to.context(self.driver.contexts[-1])
        self.driver.swipe(500,1800,500,300)
        self.driver.find_element_by_xpath("//*[@text='天气地图']").click()

    def test_dev(self):
        self.driver.get_screenshot_as_file("./test.png")