from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    guitar_model = models.CharField(max_length=35, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'









# BEGINNER = 'BEG'
#     INTERMEDIATE = 'INT'
#     ADVANCED = 'ADV'
#     NEW_PLAYER = 'NEW'
#     GUITAR_PLAYING_LEVEL = [
#         (BEGINNER, 'Beginner'),
#         (INTERMEDIATE, 'Intermediate'),
#         (ADVANCED, 'Advanced'),
#         (NEW_PLAYER, 'New Player')
#     ]
