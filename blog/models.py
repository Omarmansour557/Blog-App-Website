
from django.db import models
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    date = models.DateField(blank=True, auto_now_add=True, null=True)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    name = models.CharField(max_length=255, null=True)
    post = models.ForeignKey(Post, related_name="comments",
                             on_delete=models.CASCADE)

    date = models.DateField(blank=True, null=True, auto_now_add=True)
    body = models.TextField(null=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

    def get_absolute_url(self):
        return reverse("add_comment", kwargs={"pk": self.pk})
