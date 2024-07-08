from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from blog.models import Post, Category
from django.contrib.auth.models import User


# Create your tests here.
class PostTests(APITestCase):
    
    def test_view_posts(self):
        url = reverse('blog_api:list-create')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_post(self):
        self.test_category = Category.objects.create(name='django')
        self.test_user = User.objects.create_user(username='test_user', password='12345567890')
        
        data = {
            'title': 'new',
            'author': 1,
            'excerpt': 'new',
            'content': 'new',
        }
        url = reverse('blog_api:list-create')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_post_update(self):
        client = APIClient()
        self.test_category = Category.objects.create(name='django')
        self.test_user = User.objects.create_user(username='test_user', password='1234567890')
        self.test_user2 = User.objects.create_user(username='test_user2', password='1234567890')
        
        test_post = Post.objects.create(
            category_id=1, title='new', excerpt='new', content='some content here',
            author_id=1, slug='new',
            status=Post.Status.DRAFT
        )
        
        client.login(username=self.test_user.username, password='1234567890')
        url = reverse('blog_api:detail-create', kwargs={'pk': 1})
        response = client.put(
            url,
            {
                'id': 1,
                'title': 'new',
                'author': 1,
                'excerpt': 'excerpt',
                'content': 'new',
                'status': 'Published',
            },
            format='json'
        )
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        