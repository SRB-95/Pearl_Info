from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    image = models.ImageField(default='https://png.pngtree.com/png-clipart/20190629/original/pngtree-vector-edit-profile-icon-png-image_4102545.jpg', upload_to='profile_pictures')
    location = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return self.user.username
