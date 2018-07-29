# -*- coding:utf-8 -*-
from django.contrib import admin
from django.conf import settings
from django.urls import reverse
from django.utils.html import format_html

from base.admin import CustomAdmin
from .models import Salary, SalaryList


class SalaryListAdmin(CustomAdmin):
    list_display = ['department', 'user_full_name', 'get_product', 'amount', 'create_date', 'status', ]
    search_fields = ['user__username', 'user__full_name', 'amount']
    list_filter = ['create_date', 'status']
    ordering = ['-create_date']
    list_display_links = None

    def has_add_permission(self, request):
        return False

    def get_record(self, obj):
        user_department = obj.user.department
        if user_department == 2:
            record = obj.recordTailor
        elif user_department == 3:
            record = obj.recordSew
        elif user_department == 4:
            record = obj.recordiron
        else:
            record = "NULL"
        return record

    def department(self, obj):
        return settings.USER_GROUP.get(obj.user.department)

    def user_full_name(self, obj):
        return obj.user.full_name

    def get_product(self, obj):
        if obj.user.department in (2,3,4):
            record = self.get_record(obj)
            if obj.user.department == 2:
                return obj.recordTailor
                # return "test"
            # elif obj.user.department in (3, 4):
            #     return record.productBid.recordTailor.product
            else:
                return "NULL"

    # def get_number(self, obj):
    #     record = self.get_record(obj)
    #     return record.number

    # def inrecordData(self, obj):
    #     inrecord = obj.inrecord
    #     link = reverse("admin:records_inrecord_change", args=(inrecord.id,))
    #     a_text = "{} 件 {} - {}".format(inrecord.number, inrecord.product.name, inrecord.create_date.date())
    #     return format_html('<a target="_blank" href="%s">%s</a>' % (link, a_text))

    department.short_description = u'部门'
    user_full_name.short_description = u'员工'
    get_product.short_description = u'产品'
    # get_number.short_description = u'数量'
    # inrecordData.short_description = u'关联入库记录'


class SalaryAdmin(CustomAdmin):
    list_display = ['month', 'user_full_name', 'amount', 'status']
    search_fields = ['user', 'amount', 'user__full_name']
    list_filter = ['month', 'status']
    list_display_links = None
    ordering = ['-month', 'user']
    list_editable = ['status']

    def has_add_permission(self, request):
        return False

    def user_full_name(self, obj):
        return obj.user.full_name

    user_full_name.short_description = u'员工'


admin.site.register(Salary, SalaryAdmin)
admin.site.register(SalaryList, SalaryListAdmin)
