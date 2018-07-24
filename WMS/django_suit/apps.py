from django.apps import AppConfig

from django.contrib import admin

from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem

admin.site.site_header = "WMS"

class SuitConfig(DjangoSuitConfig):
    menu = (
        ParentItem('用户', children=[
            ChildItem(model='users.user'),

        ], icon='fa fa-leaf'),
        ParentItem('产品', children=[
            ChildItem(model='products.product'),
            ChildItem(model='products.productcategory'),
        ], icon='fa fa-leaf'),
        ParentItem('仓库管理', children=[
            ChildItem(model='inventory.inrecord'),
            ChildItem(model='inventory.outrecord'),
            ChildItem(model='inventory.warehouse'),
        ], icon='fa fa-users'),
        ParentItem('工资记录', children=[
            ChildItem(model='salary.salarylist'),
            ChildItem(model='salary.salary'),

            # 通用view
            # ChildItem('Open Google', url='http://google.com', target_blank=True),

        ], icon='fa fa-cog'), # align_right=True,),
    )
