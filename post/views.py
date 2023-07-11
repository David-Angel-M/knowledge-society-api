from rest_framework.generics import ListAPIView, DestroyAPIView, RetrieveAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.views import APIView
from .serializers import PostListSerializer, PostSerializer, CategoryListSerializer
from .models import Post, Category
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response


class PostListProv(ListAPIView):
    serializer_class = PostListSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Post.objects.all()
        else:
            user_id = self.request.user.id
            return Post.objects.filter(user_id=user_id)


class PostCreateProv(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def post(self, request):
        serializer = PostSerializer(data=request.data)

        if request.user.is_verified:
            if serializer.is_valid():
                serializer.save(user=self.request.user)
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class PostDetailProv(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

    def get(self, request, id):
        post = self.get_object(id)
        if self.has_object_permission(request, post):
            serializer = PostSerializer(post)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def put(self, request, id):
        post = self.get_object(id)
        if self.has_object_permission(request, post):
            serializer = PostSerializer(post, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def get_object(self, id):
        try:
            return Post.objects.get(id=id)
        except Post.DoesNotExist:
            return None

    def has_object_permission(self, request, post):
        if post and (str(post.user.id) == str(request.user.id) or request.user.is_superuser):
            return True
        return False


class PostDeleteProv(DestroyAPIView):  
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'


class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = ()

# Delete
# Testing the CRUD without Token
class PostCreate(CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = ()

# Replace by RetrieveAPIView
# Testing the CRUD without Token
class PostDetail(RetrieveUpdateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = ()
    lookup_field = 'id'

# Delete
# Testing the CRUD without Token
class PostDelete(DestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = ()
    lookup_field = 'id'


class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = ()
