from django.db import models

# Create your models here.
class ChatModel(models.Model):

    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # class Meta:
    #     ordering = ('created',)

    def __str__(self):
        return self.email