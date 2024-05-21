from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post

class PostModelTest(TestCase):

    def setUp(self):
        # Create a User object
        self.user = User.objects.create_user(username='TestUser', email='test@example.com', password='testpass')
        
        # Create a Post object for testing
        self.post = Post.objects.create(title='Test Post', content='This is a test post.', author=self.user)

    def test_post_has_title(self):
        # Test that a Post object has the expected title
        post = Post.objects.get(id=self.post.id)
        self.assertEqual(post.title, 'Test Post')

    def test_post_has_content(self):
        # Test that a Post object has the expected content
        post = Post.objects.get(id=self.post.id)
        self.assertEqual(post.content, 'This is a test post.')

class PostViewTest(TestCase):

    def setUp(self):
        # Create a User object
        self.user = User.objects.create_user(username='TestUser', email='test@example.com', password='testpass')
        
        # Log in the user
        self.client.login(username='TestUser', password='testpass')

        # Create a Post object for testing views
        self.post = Post.objects.create(title='Test Post', content='This is a test post.', author=self.user)

    def test_post_list_view(self):
        # Test the post-list view
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_post_detail_view(self):
        # Test the post-detail view
        response = self.client.get(reverse('post_detail', args=[str(self.post.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
        self.assertContains(response, 'This is a test post.')

class UserAuthTest(TestCase):

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Register')

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Login')

    def test_user_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful registration
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_user_login(self):
        User.objects.create_user(username='testuser', email='test@example.com', password='testpass')
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful login
