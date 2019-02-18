from django.db import models

# Create your models here.

#create a blog model
   #title
   #pub_date
   #body
   #image


class blog(models.Model):
    title = models.CharField(max_length=100)
    bub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

# add the blog app to the setting

# create a migreations

# migrate

# add to the admin

