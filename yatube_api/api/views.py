# TODO:  Напишите свой вариант
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)
