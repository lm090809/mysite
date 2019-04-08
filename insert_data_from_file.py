from django.core import serializers
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

'''
Django 版本大于等于1.7的时候，需要加上下面两句
import django
django.setup()
否则会抛出错误 django.core.exceptions.AppRegistryNotReady: Models aren't loaded yet.
'''

import django
import json

if django.VERSION >= (1, 7):  # 自动判断版本
    django.setup()


def main():
    from analysis.models import User
    f = open('F:\work2\mysite\datafile', encoding='utf-8')
    for line in f:
        name, pwd, email, type = line.split('|')
        User.objects.create(username=name, userpass=pwd, useremail=email, usertype=type)
    f.close()


def jsondb():
    from analysis.models import User
    data = eval(serializers.serialize("json", User.objects.all()))  # json
    userdata = json.dumps(data)
    print(type(userdata))


if __name__ == "__main__":
    main()
    # jsondb()
    print('插入完毕!')