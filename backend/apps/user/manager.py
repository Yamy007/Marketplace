from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self,email, password, **kwargs):
        email = self.normalize_email(email=email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user 
    
    