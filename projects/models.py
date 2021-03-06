from django.db import models
import uuid

from users.models import Profile


class Project(models.Model):
    """
    Project of a programmer with connected:
        - Owner
        - Tags
        - Reviews
    """

    owner = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to="projects/", default="projects/default.jpg", null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)

    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-vote_ratio', '-vote_total', 'title']

    @property
    def reviewers(self):
        reviewers = self.review_set.all().values_list('owner__uuid', flat=True)
        return reviewers

    @property
    def get_vote_statistics(self):
        reviews = self.review_set.all()

        up_votes = reviews.filter(vote='up').count()
        vote_total = reviews.count()
        vote_ratio = (up_votes / vote_total) * 100

        self.vote_total = vote_total
        self.vote_ratio = vote_ratio
        self.save()


class Review(models.Model):
    """
    Project's review by a user with:
        - Owner
        - Project
        - Comment   - body
        - Vote mark - up/down
    """

    VOTE_CHOICES = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )

    owner = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)
    vote = models.CharField(max_length=255, choices=VOTE_CHOICES)

    created_date = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )

    class Meta:
        unique_together = [['owner', 'project']]

    def __str__(self):
        return self.vote


class Tag(models.Model):
    """
    Tag that contains the name of technology.

    Many-to-Many relationship to:
        - Projects
        - Users as Skills
    """
    name = models.CharField(max_length=255)

    created_date = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
    )

    def __str__(self):
        return self.name
