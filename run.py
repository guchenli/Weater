# -*- coding: utf-8 -*-
# @author: GuChenLi
# @time: 2022-10-13
# @File: run.py

import shutil
import time
import pytest
from Common import Log
from config.dir_config import report_dir
from Common.shell import Shell

xml_report_path = report_dir + "/xml"
html_report_path = report_dir + "/html"
tm = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime(time.time()))

if __name__ == '__main__':
    log = Log.MyLog()
    log.info("-----------------------------START: %s----------------------------------" % tm)
    shutil.rmtree(xml_report_path)
    mark = 'home'  # 指定标签
    args = ['-s', '-v', f'-k {mark}','--alluredir', xml_report_path]
    pytest.main(args)
    cmd = 'allure generate %s -o %s --clean' % (xml_report_path, html_report_path)
    Shell.shell(cmd)
    log.info("-----------------------------END: %s------------------------------------" % tm)
