from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from products.models import Product

class ProductUpdateTestCase(APITestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name='Test Product',
            description='Test description ...',
            price=100.0
        )

        self.update_url = reverse('product-update', kwargs={'pk': self.product.id})

    def test_case_1(self):
        update_data = {
            'name': 'Updated Product',
            'description': 'Updated description ...',
            'price': 150.0
        }

        response = self.client.put(self.update_url, data=update_data, format='json')
        self.product.refresh_from_db()# refresh the data from the database
        # Checks the data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.product.name, update_data['name'])
        self.assertEqual(self.product.description, update_data['description'])
        self.assertEqual(self.product.price, update_data['price'])

        print("Test case 1 Successful")
    
    def test_case_2(self):
        update_data = {
            'description': 'Updated New description ...'
        }
        response = self.client.patch(self.update_url, data=update_data, format='json')
        self.product.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.product.description, update_data['description'])
        print("Test case 2 successful")

    def test_case_3(self):
        update_data = {
            'name': 'Test Product',
            'description': 'new description ...',
            'price': None
        }

        response = self.client.put(self.update_url, data=update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('price', response.data)

        print("Test case 3 successful")
        

