# -*- coding:utf-8 -*-

# Created by Dolphin on 18-7-24

import random

from .models import User


def create_superuser(username, password="00000", department=1):
    User.objects.create(username=username, password=password, department=department, status=1, is_staff=1, is_active=1, is_superuser=1)


def set_password(id, password):
    user = User.objects.get(pk=id)
    user.set_password(password)
    user.save()


def create_user(username, password="00000", department=None):
    User.objects.create(username=username, password=password, status=1, department=department, is_staff=0, is_active=1, is_superuser=0)


def gen_fake():
    for x in range(1000, 1200):
        username = "1551888" + str(x)
        group = random.randint(2, 5)
        create_user(username=username, password="123456", department=group)
