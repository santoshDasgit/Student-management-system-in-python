
# from django.contrib.auth import get_user_model
# from django.contrib.auth.backends import ModelBackend

# class EmailBackend(ModelBackend):
#     def authenticate(self, username=None, password=None ,**kwargs):
#         data = get_user_model()
#         try:
#             user = data.objects.get(email=username)
#         except data.DoesNotExist:
#             return None
#         else:
#             if user.check_password(password):
#                 return user
#         return None
            
      
