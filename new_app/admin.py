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


class MyModelAdmin(admin.ModelAdmin):
    exclude = ('user_id',)

    def save_model(self, request, obj, form, change):
        obj.user_id = request.user
        obj.save()


admin.site.unregister(User)

admin.site.register(Track, MyModelAdmin)
admin.site.register(Question,MyModelAdmin)
admin.site.register(Answer,MyModelAdmin)
admin.site.register(Material, MyModelAdmin)
admin.site.register(Post, MyModelAdmin)
admin.site.register(User,SiteUserAdmin)


