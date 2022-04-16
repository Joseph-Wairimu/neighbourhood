from django.test import TestCase

from .models import User,NeighborHood,Business
from django.contrib.auth.models import User

# Create your tests here.
class BusinessTest(TestCase):
    def setUp(self):
        self.user=User.objects.create_user('testuser')
        self.neighborhood=NeighborHood.objects.create(name='testneighborhood',location='testlocation',occupants_count=0,admin=self.user)
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
