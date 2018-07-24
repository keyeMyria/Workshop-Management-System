# -*- coding:utf-8 -*-

# Created by Dolphin on 18-7-24

from .models import User


def create_superuser(username, password):
    User.objects.create(username=username, password=password, status=1,)


def set_password(id, password):
    user = User.objects.get(pk=id)
    user.set_password(password)
    user.save()
