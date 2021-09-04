from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='d.jpg', upload_to='profile_pic')

    def __str__(self):
        return self.user.username

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            outsize = (300, 300)
            img.thumbnail(outsize)
            img.save(self.image.path)


