# coding = utf8
import os

from django.http import HttpResponse
from django.shortcuts import render

os.path.abspath(".")
"""
    @File:views.py
    @Author:Bruce
    @Date:2022/12/16
"""


def hello(request):
    return HttpResponse("Hello World!")


def index(request):
    return HttpResponse("主页")


def runoob(request):
    context = {}
    context["hello"] = "Hello World!"
    context["explain"] = "这是映射键值对数据," \
                         "由html模版中对应的{{hello}}标签映射"
    view_list = ["列表元素1", "列表元素2", "列表元素3"]
    context["view_list"] = view_list
    view_dict = {"name": "字典元素1", "age": "字典元素2", "salary": "字典元素3"}
    context["view_dict"] = view_dict
    # context["cgtisthebest"] = "1"
    context["num"] = 19073741824
    context["link1"] = "/index"
    context["link2"] = "http://www.baidu.com"
    return render(request, "runoob.html", context)
