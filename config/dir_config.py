# -*- coding: utf-8 -*-
# @author: GuChenLi
# @time: 2022-10-13

import os
#框架项目顶层目录

base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]  # D:\Desktop\Weater

test_data_dir = os.path.join(base_dir,"Data")

testcases_dir = os.path.join(base_dir,"TestCases")

report_dir = os.path.join(base_dir,"outputs/report")

logs_dir = os.path.join(base_dir,"Outputs/logs")

screenshot_dir = os.path.join(base_dir,"Outputs/screenshots")
