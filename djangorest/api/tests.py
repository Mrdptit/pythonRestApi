from django.test import TestCase
from rest_framework.test    import APIClient
from rest_framework         import status
from django.core.urlresolvers import reverse
# Create your tests here.

class viewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.bucketlist_data    =   {'name' : 'Hello would'}
        self.response   =   self.client.post(
           reverse('create'),
           self.bucketlist_data,
           format = 'json'
        )
    def test_apis(self):
        
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
    def test_api_can_get(self):
        
        bucketlist = Bucketlist.objects.get()
        response    =   self.client.get(
            reverse('details',kwargs={'pk' : bucketlist.id}), format = "json"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, bucketlist)
    def test_api_can_update(self):
        change_bucketlist = {'name' : 'Something new'}
        res = self.client.put(
            reverse('details', kwargs= {'pk': bucketlist.id}),
            change_bucketlist, format= 'json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    def test_api_can_delete(self):
        
        bucketlist  =   Bucketlist.objects.get()
        response    =   self.client.delete(
            reverse('details', kwargs={'pk': bucketlist.id}),
            format= 'json',
            follow= True
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
