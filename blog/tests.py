from django.test import TestCase
from django.test import Client

# Create your tests here.

c = Client()

response = c.get('/')
response.status_code


class Mytest(Client):
    def test_detail(self):
        response = self.client.get('/blog/post_list.html')
        print(response['location'])
        self.assertEqual(response.status_code, 200)
