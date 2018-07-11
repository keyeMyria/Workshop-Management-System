# -*- coding:utf-8 -*-

# -*- coding:utf-8 -*-
from salary.models import SalaryList

def set_salary(obj):
    group_flag = obj.employee.group.flag
    if group_flag == 2:
        amount = obj.number * obj.product.cj_price
    elif group_flag == 4:
        amount = obj.number * obj.product.yt_price
    elif group_flag == 3:
        amount = obj.number * obj.product.fr_price
    elif group_flag == 5:
        amount = obj.number * obj.product.bz_price
    else:
        # 该员工不属于该计工资规则
        pass
    saralylist = SalaryList.objects.filter(inrecord=obj).first()

    if saralylist is not None:
        saralylist.amount = amount
        saralylist.save(update_fields=['amount'])
    else:
        saralylist = SalaryList.objects.create(employee=obj.employee,create_date=obj.create_date, inrecord=obj, amount=amount)
    saralylist.save()


# 生成虚拟数据

import random
import datetime
from employees.models import Employee
from products.models import Product
from .models import Warehouse
from .models import InRecord
from django.utils import timezone


def gen_fake(num):
    employees = Employee.objects.all()
    products = Product.objects.all()
    date = timezone.datetime.now(tz=timezone.utc)
    for x in range(num):
        number = random.randint(5, 30)
        create_date = date - datetime.timedelta(days=random.randint(0, 90))
        employee = employees[random.randint(0, len(employees)-1)]
        product = products[random.randint(0, len(products)-1)]
        obj = InRecord.objects.create(employee=employee, product=product, status_number=number, number=number, create_date=create_date)
        ware = Warehouse.objects.filter(product=obj.product).first()
        if ware is not None:
            ware.number += obj.number
        else:
            ware = Warehouse.objects.create(product=obj.product, number=obj.number)
        ware.save()

        group_flag = obj.employee.group.flag
        if group_flag == 2:
            amount = obj.number * obj.product.cj_price
        elif group_flag == 4:
            amount = obj.number * obj.product.yt_price
        elif group_flag == 3:
            amount = obj.number * obj.product.fr_price
        elif group_flag == 5:
            amount = obj.number * obj.product.bz_price
        else:
            # 该员工不属于该计工资规则
            pass
        saralylist = SalaryList.objects.filter(inrecord=obj).first()

        if saralylist is not None:
            saralylist.amount = amount
            saralylist.save(update_fields=['amount'])
        else:
            saralylist = SalaryList.objects.create(employee=obj.employee, create_date=obj.create_date, inrecord=obj, amount=amount)
        saralylist.save()
