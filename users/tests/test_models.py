from rest_framework.test import APITestCase
from users.models import User


class TestModel(APITestCase):
    
    def test_create_user(self):
        user=User.objects.create_user(username='username1', email='chessreynolds+3@gmail.com', password='Karatechop1!')
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, 'chessreynolds+3@gmail.com')
        self.assertFalse(user.is_staff)
        
    def test_create_superuser(self):
        user=User.objects.create_superuser(username='username1', email= 'chessreynolds+3@gmail.com', password='Karatechop1!')
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, 'chessreynolds+3@gmail.com')
        self.assertTrue(user.is_staff)
        
    def test_raises_error_when_no_username_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user, username="", email="chessreynolds+3@gmail.com", password="Karatechop1!")
        
    def test_raises_error_with_message_when_no_username_supplied(self):
        with self.assertRaisesMessage(ValueError, 'Username required'):
            User.objects.create_user(username="", email="chessreynolds+3@gmail.com", password="Karatechop1!")
    
    def test_raises_error_when_no_email_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user, username="username1", email="", password="Karatechop1!")
        
    def test_raises_error_with_message_when_no_email_supplied(self):
        with self.assertRaisesMessage(ValueError, 'Email required'):
            User.objects.create_user(username="Username1", email="", password="Karatechop1!")
            
    def test_raises_error_when_superuser_is_not_staff(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True'):
            User.objects.create_superuser(username="Username1", email="", password="Karatechop1!", is_staff=False)
            
    def test_raises_error_when_superuser_is_not_superuser(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True'):
            User.objects.create_superuser(username="Username1", email="", password="Karatechop1!", is_superuser=False)
            
    
    
    