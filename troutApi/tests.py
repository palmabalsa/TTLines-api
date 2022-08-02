# from rest_framework.test import APITestCase
# from django.urls import reverse
# from rest_framework import status
# from trout.models import FishingLogEntry
# from users.urls import UserRegistration, LoginUser


# # test for:
# # status code/endpoint works
# # if you are able to send a datapoint, is it the same one that you get sent back from server?
# # if you create an item, does the db recieve the update? etc
# # (eg: check the db item count prior to your create, then check it after and make sure its +1 )
# # 


# class LogEntryAPITestCaseSetUp(APITestCase):
#     def create_log_entry(self):
#         sample_log_entry = {"river_pool": "breakfast",
#                             "fly_used": "wooly bugger",
#                             "any_notes": "high river"}
#         response = self.client.post(reverse('create'), sample_log_entry)
#         return response

#     def authenticate(self):
#         self.client.post(
#             reverse("registration"), {"username": "username", 
#                                   "email":"email@gmail.com", "password": "password"})
#         response = self.client.post(
#             reverse("login"), {"email": "email@gmail.com", 
#                                "password": "password"})
#         self.client.credentials(HTTP_AUTHORIXATION=f"Bearer {response.data['token']}")



# class TestEditOrDeleteLogEntry(LogEntryAPITestCaseSetUp):
    
#     def test_edit_one_log_entry(self):
#         self.authenticate()
#         response=self.create_log_entry()
        
#         res=self.client.patch(
#             reverse("log", kwargs={'id':response.data['id']}),{
#             "river_pool": "newData",
#             # "fly_used": "newData",
#             "any_notes": "newData"
#             })
#         self.assertEqual(res.status_code, status.HTTP_200_OK)
    
#         patched_entry = FishingLogEntry.ojects.get(id= response.data['id'])
        
#         self.assertEqual(patched_entry.river_pool, "newData")
#         # self.assertEqual(patched_entry.fly_used, "newData")
#         self.assertEqual(patched_entry.any_notes, "newData")
 
    
#     def test_deletes_one_log_entry(self):
#         self.authenticate()
#         self.create_log_entry()
#         previous_db_count= FishingLogEntry.objects.all().count()
        
#         self.assertGreater(previous_db_count, 0)
#         self.assertEqual(previous_db_count, 1)
        
#         response.self.client.delete(reverse(""))

# this would work if i had listcreate as one api endpoint, but becasue i am doing
# them seperatly, the reverse isnt working


# class TestCreateLogEntry(LogEntryAPITestCaseSetUp):  
#     def test_create_log_entry_shouldnt_work_beacause_no_auth(self):
#         response = self.create_log_entry()
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
     
#     def test_create_log_entry_should_succeed(self):
#         self.authenticate()
#         response = self.create_log_entry()
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)    