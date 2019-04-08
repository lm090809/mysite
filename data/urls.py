from django.conf.urls import re_path
from . import views
# 使用了二级路由

app_name = 'data'
urlpatterns = [

    re_path(r'^index/', views.index, name='index'),                            # 主页
    re_path(r'^test_page', views.test_page, name='test_page'),                 # 测试页面
    re_path(r'^lists/(?P<table>\w+)/$', views.lists, name='lists'),            # 数据解析页面
    re_path(r'^diagnosis/', views.diagnosis, name='diagnosis'),                # 故障诊断页面
    re_path(r'^engine_fault_code_data/$', views.engine_fault_code_data),       # 全部的故障码数据
    re_path(r'^engine_fault_data_reload/$', views.engine_fault_data_reload),   # 查询的故障码和现象数据

]