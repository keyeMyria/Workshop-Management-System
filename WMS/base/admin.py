from django.contrib import admin

class CustomAdmin(admin.ModelAdmin):

    list_per_page = 30
    actions_on_top = True
    actions_on_bottom = False

    def has_delete_permission(self, request, obj=None):
        return False
