from django.shortcuts import get_object_or_404
from rest_framework.viewsets import (GenericViewSet,
                                     ModelViewSet,
                                     ReadOnlyModelViewSet)
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from posts.models import Comment, Follow, Group, Post
from .serializers import (CommentSerializer,
                          FollowSerializer,
                          GroupSerializer,
                          PostSerializer)
from .permissions import IsAuthorOrReadOnly


class ListCreateViewSet(ListModelMixin, CreateModelMixin, GenericViewSet):
    pass


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        comments = Comment.objects.filter(post=post_id)
        return comments

    def perform_create(self, serializer):
        post_obj = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return serializer.save(author=self.request.user, post=post_obj)


class GroupViewSet(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (AllowAny,)


class FollowViewSet(ListCreateViewSet):
    serializer_class = FollowSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        request_user = self.request.user
        following = Follow.objects.filter(user=request_user)
        return following

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
