from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings

# Create your models here.

class Post(models.Model):
    status = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='posts/%Y/%m/%d',blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='posts_liked',blank=True)
    class Meta:
        ordering = ('created',)
        index_together = (('id'),)

    def __str__(self):
        return self.status

    def get_absolute_url(self):
        return reverse('posts:post_detail',args=[self.id])

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)