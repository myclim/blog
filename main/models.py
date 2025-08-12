from django.db import models
from core import settings



class Posts(models.Model):
    title = models.CharField(max_length=300, unique=True, verbose_name='title')
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='user', related_name='posts' )
    text = models.TextField(verbose_name='text')
    views = models.SmallIntegerField(default=0, verbose_name='Колличество просмотров')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user_posts"
        ordering = ['-create_at']
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'

    def __str__(self):
        return f'{self.user}: {self.title}'
