# from django.test import TestCase
# from rest_framework import status

# from user.models.user_model import UserModel
# from rest_framework.test import APIClient

# # Create your tests here.
# class ApiTest(TestCase):
#     def test_get_simulations_without_token(self):
#         response = self.client.get('/api/v1/simulations/')
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
#     def test_get_simulations_with_token(self):
#         user = UserModel.objects.get(username='lauren')
#         client = APIClient()
#         client.force_authenticate(user=user)
#         respoms