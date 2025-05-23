from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from products.models import Product

class ProductCreateTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('product-create')
        self.data = {
            'name': 'Test Product',
            'description': 'Test description ...',
            'price': 100.0
        }

    def test_case_1(self): # Successfully create an object
        response = self.client.post(self.url, data=self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, self.data['name'])
        print("Test case 1 successfull")

    def test_case_2(self): # Return 400 bad request
        data ={
            'name': 'Test Product',
            'description': None,
            'price': 100.0
        }
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('description', response.data)
        self.assertIn('This field may not be null.', response.data['description'])
        print("Test case 2 successfull")


        

