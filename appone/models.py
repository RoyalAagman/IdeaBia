from django.db import models
from sorl.thumbnail import ImageField
from django.contrib.auth.models import User

class Post(models.Model):
    text = models.CharField(max_length = 150, blank = True, null = True) 
    # caption for Image to be added
    image = ImageField()
    # For Image to be added 
    author = models.ForeignKey(User , on_delete= models.CASCADE, null=True)
    # author added : to display the name the name of user who has posted the post
    date = models.DateTimeField(auto_now=True)
    # date field added : to display the date the post was added
  
    # function added to display text on the database table inside admin block
    def __str__(self):
        return self.text