# -*- coding: utf-8 -*-
# @author: GuChenLi
# @time: 2022-10-13

import yaml

from config.dir_config import  test_data_dir


def get_data():
    with open(test_data_dir + "\\" + "data_city.yaml", encoding="utf-8") as f:
        data = yaml.safe_load(f)
        return data

print(get_data())