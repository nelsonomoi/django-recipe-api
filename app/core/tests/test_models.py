from django.test import TestCase
from django.contrib.auth import get_user_model




class ModelTests(TestCase):
    """Test user creation model"""
    def test_create_user_model(self):

        email = 'omoinelson32gmail.com'
        password = 'abcd123'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password)) 


    def test_create_user(self):
        pass

        # user = get_user_model().objects.create_user(
        #     email = 'omoinelson3@gmail',
        #     password = 'test_123'
        # )

        # self.assertEqual(user.email,'omoinelson3@gmail.com')