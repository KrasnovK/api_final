from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions, viewsets

import api

from .models import Comment, Follow, Group, Post, User
from .permissions import IsAuthorOrReadOnly
from .serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer,
)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        api.permissions.IsAuthorOrReadOnly,
    )
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "group",
    ]

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        api.permissions.IsAuthorOrReadOnly,
    )

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get("post_id"))
        return post.comments

    def perform_create(self, serializer):
        get_object_or_404(Post, id=self.kwargs.get("post_id"))
        serializer.save(author=self.request.user)


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        api.permissions.IsAuthorOrReadOnly,
    )
    filter_backends = [filters.SearchFilter]
    search_fields = ["=user__username", "=following__username"]

    def perform_create(self, serializer):
        return serializer.save(
            user=self.request.user,
            following=get_object_or_404(
                User, username=self.request.POST["following"]
            ),
        )


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        api.permissions.IsAuthorOrReadOnly,
    )

    def perform_create(self, serializer):
        return serializer.save()
