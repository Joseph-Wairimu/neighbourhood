from django.test import TestCase

from .models import User,NeighborHood,Business
from django.contrib.auth.models import User

# Create your tests here.
class NeighborHoodTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.hood = NeighborHood.objects.create(name='Test', location='Test', occupants_count=0, user=self.user)

    def test_hood_instance(self):
        self.assertTrue(isinstance(self.hood, NeighborHood))

    def test_hood_creation(self):
        self.assertEqual(self.hood.name, 'Test')
        self.assertEqual(self.hood.location, 'Test')
        self.assertEqual(self.hood.occupants_count, 0)
        self.assertEqual(self.hood.user, self.user)

    def test_hood_str(self):
        self.assertEqual(str(self.hood), self.hood.name)

    def test_hood_delete(self):
        self.hood.delete()
        self.assertEqual(NeighborHood.objects.all().count(), 0)

    def test_hood_update(self):
        self.hood.name = 'Test2'
        self.hood.save()
        self.assertEqual(self.hood.name, 'Test2')


    def test_hood_update_location(self):
        self.hood.location = 'Test2'
        self.hood.save()
        self.assertEqual(self.hood.location, 'Test2')


class BusinessTest(TestCase):
    def setUp(self):
        self.user=User.objects.create_user('testuser')
        self.neighborhood=NeighborHood.objects.create(name='testneighborhood',location='testlocation',occupants_count=0,user=self.user)
    def test_create_business(self):
        business=Business.objects.create(name='testbusiness',location='testlocation',user=self.user,neighborhood=self.neighborhood)
        self.assertEqual(business.name,'testbusiness')
        self.assertEqual(business.location,'testlocation')
        self.assertEqual(business.user,self.user)
        self.assertEqual(business.neighborhood,self.neighborhood)
    def test_update_business(self):
        business=Business.objects.create(name='testbusiness',location='testlocation',user=self.user,neighborhood=self.neighborhood)
        business.name='updatedbusiness'
        business.location='updatedlocation'
        business.save()
        self.assertEqual(business.name,'updatedbusiness')
        self.assertEqual(business.location,'updatedlocation')
        self.assertEqual(business.user,self.user)
        self.assertEqual(business.neighborhood,self.neighborhood)
    def test_delete_business(self):
        business=Business.objects.create(name='testbusiness',location='testlocation',user=self.user,neighborhood=self.neighborhood)
        business.delete()
        self.assertEqual(Business.objects.count(),0)
    def test_get_business(self):
        business=Business.objects.create(name='testbusiness',location='testlocation',user=self.user,neighborhood=self.neighborhood)
        business=Business.objects.get(name='testbusiness')
        self.assertEqual(business.name,'testbusiness')
        self.assertEqual(business.location,'testlocation')
        self.assertEqual(business.user,self.user)
        self.assertEqual(business.neighborhood,self.neighborhood)
