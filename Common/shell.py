# -*- coding: utf-8 -*-
# @author: GuChenLi
# @time: 2022-10-13

"""
封装执行shell语句方法

"""

import subprocess


class Shell:
    @staticmethod
    def shell(cmd):
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        return o


