from django.contrib import admin
from .models import Organisation, OrganisationRoles, EmployeeRoles
# Register your models here.

admin.site.register(Organisation)
admin.site.register(OrganisationRoles)
admin.site.register(EmployeeRoles)
