from django.contrib.auth.models import UserManager


class GalleryUserManager(UserManager):

    def create_user(self, username, password=None, **kwargs):
        if not username:
            raise ValueError("The given username must be set")
        user = self.model(username=username, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **kwargs):
        user = self.create_user(
            username,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user