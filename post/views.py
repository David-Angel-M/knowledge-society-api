from rest_framework.generics import ListAPIView, DestroyAPIView, CreateAPIView, RetrieveUpdateAPIView
from .serializers import PostListSerializer, PostSerializer
from .models import Post

class PostListProv(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = ()

class PostCreate(CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = ()


class PostDetailProv(RetrieveUpdateAPIView):
    serializer_class = PostSerializer  
    queryset = Post.objects.all()  
    permission_classes = ()
    lookup_field = 'id'


class PostDeleteProv(DestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = ()
    lookup_field = 'id'
