from django.apps import AppConfig

from django.contrib import admin

from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem

admin.site.site_header = "六福服饰管理系统"

class SuitConfig(DjangoSuitConfig):
    menu = (
        ParentItem('用户', children=[
            ChildItem(model='users.user'),
            ChildItem('管理员组',model='auth.group'),
        ], icon='fa fa-leaf'),
        ParentItem('产品', children=[
            ChildItem(model='products.product'),
            ChildItem(model='products.productcategory'),
            ChildItem(model='products.warehouse'),
        ], icon='fa fa-leaf'),
        ParentItem('记工', children=[
            ChildItem(model='records.recordtailor'),
            ChildItem(model='records.recordsew'),
            ChildItem(model='records.recordiron'),
            ChildItem(model='records.recordoutput'),
        ], icon='fa fa-users'),
        ParentItem('工资记录', children=[
            ChildItem(model='salary.salarylist'),
            ChildItem(model='salary.salary'),

        ], icon='fa fa-cog'),  # align_right=True,),
    )
