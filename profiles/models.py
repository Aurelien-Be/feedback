from django.db import models

# Create your models here.

class UserProfile(models.Model):
    #image = models.FileField(upload_to="images")
    #images should not be stocked in a database but in hard drives
    #FileField only store the path in the database

    #better : image field (django will accept only images)
    image = models.ImageField(upload_to="images")
    #but it needs the extra package pillow
