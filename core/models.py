from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Organisation(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.name)

class OrganisationRoles(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.name)

class EmployeeRoles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='roles_user')
    organisation = models.ForeignKey(Organisation, on_delete=models.SET_NULL, null=True, related_name='roles_organisation')
    role = models.ForeignKey(OrganisationRoles, on_delete=models.SET_NULL, null=True, related_name='roles_role')

    def __str__(self):
        return '{}'.format(self.user)