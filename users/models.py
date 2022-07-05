from django.db import models
from django.contrib.auth.models import User
import uuid

# TODO: Process the null/not-null values


class Profile(models.Model):
    """
    Profile's info is directly connected to User, although User is different model. 

    We use pre-build User for authentification and profile to share info among other users. 
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)

    short_description = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(
        upload_to="users/", default="users/user-default.webp", null=True, blank=True)

    social_github = models.CharField(max_length=255, null=True, blank=True)
    social_linkedin = models.CharField(max_length=255, null=True, blank=True)
    social_youtube = models.CharField(max_length=255, null=True, blank=True)
    social_website = models.CharField(max_length=255, null=True, blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )

    def __str__(self):
        return str(self.user)

    class Meta:
        ordering = ['created_date']


class Skill(models.Model):
    """
    Skill is connected with Profile by Many-to-One relationship. 

    Defined by every user separately.
    """
    owner = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )

    def __str__(self):
        return self.name


class Message(models.Model):
    sender = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, related_name='sent_messages', null=True, blank=True)
    recipient = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, related_name='inbox_messages', null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['is_read', '-created_date']
