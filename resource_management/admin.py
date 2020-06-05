from resource_management.models.user import User
from resource_management.models import Resource, ResourceItem, Request, AccessLevel
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin


class UserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
            (None, {"fields": (
                                'name',
                                'profile_pic',
                                'gender',
                                'job_role',
                                'department',
                                'is_admin'
                              )
                    }
            ),
        )

admin.site.register(User, UserAdmin)
admin.site.register(Resource)
admin.site.register(ResourceItem)
admin.site.register(Request)
admin.site.register(AccessLevel)