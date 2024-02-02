from django.contrib.auth import get_user, get_user_model
from django.test import TestCase
from django.urls import reverse

from flowers.models import Flowers
from users.models import CustomUser

class UserRegistrations(TestCase):
    def test_create_user(self):
        self.client.post(
        reverse('users:regis'),
            data={
                'username':'admin',
                'first_name':'admin',
                'last_name':'admin',
                'email':'email@gmail.com',
                'password':'admin'
            }
        )
        # self.assertEqual(response.status_code, 200)
        user=CustomUser.objects.get(username='admin')

        self.assertEqual(user.first_name,'admin')
        self.assertEqual(user.last_name,'admin')
        self.assertEqual(user.email,'email@gmail.com')
        self.assertFalse(user.check_password('admin'))


    def test_required_fields(self):
        res=self.client.post(
            reverse('users:regis'),
            data={
                'first_name':'admin',
                'last_name':'admin'
            }
        )
        user_cnt=CustomUser.objects.count()

        self.assertEqual(user_cnt,0)
        self.assertTrue(res,'This field is required.')


    def test_email_regis(self):
        res=self.client.post(
        reverse('users:regis'),
            data={
                'username':'admin2',
                'first_name':'admin2',
                'last_name':'admin2',
                'email':'ema-il',
                'password':'admin2'
            }
        )
        user_cnt = CustomUser.objects.count()

        self.assertEqual(user_cnt, 0)
        self.assertTrue(res,'Enter a valid email address.')


    def test_double_user(self):
        user=CustomUser.objects.create_user(username='Nurjahon2',first_name='Nurjahon2')
        user.set_password('123qwerty')
        user.save()

        res = self.client.post(
            reverse('users:regis'),
            data={
                'username': 'Nurjahon2',
                'first_name': 'Nurjahon2',
                'last_name': 'Nurjahon2',
                'email': 'email@gmail.com',
                'password': '123qwerty'
            }
        )
        user_cnt = CustomUser.objects.count()
        self.assertEqual(user_cnt, 1)

        form_errors=res.context['form'].errors
        self.assertTrue(form_errors)
        self.assertIn('username',form_errors)
        self.assertIn('A user with that username already exists.',form_errors['username'])


class LoginTest(TestCase):
    def test_login(self):
        user = CustomUser.objects.create_user(username='admin123', first_name='admin')
        user.set_password('admin')
        user.save()

        response = self.client.post(
            reverse('users:login'),
            data={
                'username': 'admin123',
                'password': 'admin'
            }
        )

        user_is_authenticated =response.wsgi_request.user.is_authenticated
        self.assertTrue(user_is_authenticated)

    def test_login_username(self):
        user = CustomUser.objects.create_user(username='admin123', first_name='admin')
        user.set_password('admin')
        user.save()

        response = self.client.post(
            reverse('users:login'),
            data={
                'username': 'admin_123',
                'password': 'admin'
            }
        )

        user_is_authenticated =response.wsgi_request.user.is_authenticated
        self.assertFalse(user_is_authenticated)

    def test_login_password(self):
        user = CustomUser.objects.create_user(username='admin123', first_name='admin')
        user.set_password('admin')
        user.save()

        response = self.client.post(
            reverse('users:login'),
            data={
                'username': 'admin_123',
                'password': 'adminn'
            }
        )

        user_is_authenticated =response.wsgi_request.user.is_authenticated
        self.assertFalse(user_is_authenticated)


class UserProfileTests(TestCase):
    def test_user_profile_view(self):
        Users = get_user_model()
        user = Users.objects.create_user(username='admin1', password='testpassword')
        self.client.login(username='admin1', password='testpassword')
        response = self.client.get(reverse('users:profile'))
        self.assertEqual(response.status_code, 200)
