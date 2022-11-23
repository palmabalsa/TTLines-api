from rest_framework.test import APITestCase
from users.models import User

class TestModel(APITestCase):
    
    def test_create_django_user_w_fb_credentials(self):
        user=User.objects.create_user('y3FE5buvuPTWUFIYOosI45IYEVp1', )
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        
    def test_create_django_SuperUser_w_fb_credentials(self):
        user=User.objects.create_superuser('y3FE5buvuPTWUFIYOosI45IYEVp1', )
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        
    # def test_raise_error_when_SuperUser_is_Not_staff(self):
    #     self.assertRaises(ValueError, User.objects.create_superuser, is_staff=False)
    #     user=User.objects.create_superuser(firebase_user_id = 'y3FE5buvuPTWUFIYOosI45IYEVp1', email='chessreynolds+66@gmail.com')
        
    # def test_raise_error_when_SuperUser_is_Not_SuperUser(self):
    #     self.assertRaises(ValueError, User.objects.create_superuser, is_superuser=False)
    #     user=User.objects.create_superuser('y3FE5buvuPTWUFIYOosI45IYEVp1', )