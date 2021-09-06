from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    affiliation = models.CharField(max_length=150, null=True, blank=True)
    address = models.CharField(max_length=120, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    image = models.ImageField(upload_to='profile_pic', blank=True, null=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            if img.height > 300 or img.width > 300:
                outsize = (300, 300)
                img.thumbnail(outsize)
                img.save(self.image.path)


