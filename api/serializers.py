from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Comment, Follow, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field="username", read_only=True
    )

    class Meta:
        fields = "__all__"
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field="username", read_only=True
    )

    class Meta:
        fields = "__all__"
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True,
        default=serializers.CurrentUserDefault(),
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="username"
    )

    class Meta:
        fields = "__all__"
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(), fields=("user", "following")
            )
        ]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Group
        extra_kwargs = {"description": {"required": False}}
