# -*- coding: utf-8 -*-
# @author: GuChenLi
# @time: 2022-10-13

"""
app
"""
package_weather = "com.huawei.android.totemweather"  # 天气包名
weather = "天气"
package_permission = "com.android.permissioncontroller"  # 权限弹窗包名
package_search = "com.huawei.search"

"""
activity
"""
activity_home = ".WeatherHome"  # 首页
activity_permission_PUW = "com.android.packageinstaller.permission.ui.GrantPermissionsActivity"  # 权限弹窗
activity_search = ".HomeActivity"  # 智慧搜索
"""
resource-id
"""
id_disagree_btn_china = package_weather + ":" + "id/disagree_btn_china"  # 欢迎页取消
id_agree_btn_china = package_weather + ":" + "id/agree_btn_china"  # 欢迎页同意
id_search_src_text = package_weather + ":" + "id/search_src_text"  # 搜索框
id_header_more = package_weather + ":" + "id/header_more"  # 右上角菜单
id_head_progressBar = package_weather + ":" + "id/head_progressBar"  # 刷新按钮
id_addcity_item_textview = package_weather + ":" + "id/addcity_item_textview"  # 搜索结果 城市
id_current_temprature = package_weather + ":" + "id/current_temprature"  # 实况天气


id_permission_allow_foreground_only_button = package_permission + ":" + "id/permission_allow_foreground_only_button"
id_permission_allow_always_button = package_permission + ":" + "id/permission_allow_always_button"
id_permission_deny_button = package_permission + ":" + "id/permission_deny_button"

"""
text
"""
manage_cities = "管理城市"
weather_widget = "桌面天气"
theme = "个性换肤"
report_error = "反馈当前天气"
share = "分享"
settings = "设置"
add_city = "添加城市"

"""
toast 
"""
class_toast = "android.widget.Toast"
toast_report_weather = "提交成功，感谢您的反馈"

"""
推荐城市
"""
city_list = ["北京","上海","重庆","广州","成都","深圳","杭州","","","","","","","","","","","","","","","",""]