from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField("Название группы", max_length=200)
    description = models.TextField("Описание", max_length=500)

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts"
    )
    group = models.ForeignKey(
        Group,
        verbose_name="Группа",
        on_delete=models.SET_NULL,
        related_name="posts",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    text = models.TextField()
    created = models.DateTimeField(
        "Дата добавления", auto_now_add=True, db_index=True
    )


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="follower",
        blank=True,
        null=True,
    )
    following = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="following",
        blank=True,
        null=True,
    )

    class Meta:
        unique_together = ("user", "following")
