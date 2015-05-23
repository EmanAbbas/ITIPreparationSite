from django.contrib import admin
from models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.

class SiteUserInline(admin.StackedInline):
    model = SiteUser
    can_delete = False
    verbose_name_plural = 'Users'

class SiteUserAdmin(UserAdmin):
    inlines = (SiteUserInline,)



admin.site.unregister(User)

admin.site.register(Track)
admin.site.register(Question)
admin.site.register(Material)
admin.site.register(Post)
admin.site.register(User,SiteUserAdmin)


