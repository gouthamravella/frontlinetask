from django.test import TestCase
from django.contrib.auth.models import User
from .models import Organisation, OrganisationRoles, EmployeeRoles
# Create your tests here.

class OrganisationTestCase(TestCase):
    def setUp(self) -> None:
        print('Running the OrganisationTestCase')
        Organisation.objects.create(name='DadyIn Co')
        Organisation.objects.create(name='Polyplast Inc')
    
    def test_organisation_creation(self):
        dadyIn = Organisation.objects.get(name='DadyIn Co')
        poly = Organisation.objects.get(name='Polyplast Inc')
        self.assertEqual(dadyIn.name,'DadyIn Co')
        self.assertEqual(poly.name,'Polyplast Inc')
        print('Ending the OrganisationTestCase')

class OrganisationRolesTestCase(TestCase):
    def setUp(self) -> None:
        print('Running the OrganisationRolesTestCase')
        OrganisationRoles.objects.create(name='Manager')
        OrganisationRoles.objects.create(name='Assistant')
        OrganisationRoles.objects.create(name='Admin')
    
    def test_organisation_creation(self):
        manager = OrganisationRoles.objects.get(name='Manager')
        assistant = OrganisationRoles.objects.get(name='Assistant')
        admin = OrganisationRoles.objects.get(name='Admin')
        self.assertEqual(manager.name,'Manager')
        self.assertEqual(assistant.name,'Assistant')
        self.assertEqual(admin.name,'Admin')
        print('Ending the OrganisationRolesTestCase')

class EmployeeRolesTestCase(TestCase):
    def setUp(self) -> None:
        print('Running the EmployeeRolesTestCase')
        user=User.objects.create_user('doe','doe@xyz.com','Test@1234')
        organisation = Organisation.objects.create(name='DadyIn Co')
        manager = OrganisationRoles.objects.create(name='Manager')
        EmployeeRoles.objects.create(user=user, organisation=organisation, role=manager)
    
    def test_organisation_creation(self):
        user = User.objects.get(username='doe')
        employeeRoles = EmployeeRoles.objects.filter(user=user).first()
        self.assertEqual(employeeRoles.organisation.name,'DadyIn Co')
        self.assertEqual(employeeRoles.role.name,'Manager')
        print('Ending the EmployeeRolesTestCase')
