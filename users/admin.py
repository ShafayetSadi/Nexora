from django.contrib import admin

from users.models import User


@admin.register(User)
class Admin(admin.ModelAdmin):
    pass
