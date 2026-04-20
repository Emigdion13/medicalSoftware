from django.contrib import admin
from roles.models import Role


class RoleAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)


admin.site.register(Role, RoleAdmin)
