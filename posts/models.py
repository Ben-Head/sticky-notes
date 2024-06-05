from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    # Define the Post model with the following fields:
    title = models.CharField(max_length=255)  # Title of the post
    content = models.TextField()  # Content of the post
    created_at = models.DateTimeField(auto_now_add=True)  # Date and time when the post was created
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Author of the post, linked to a User object

    def __str__(self):
        # Return the title of the post when converted to a string
        return self.title
