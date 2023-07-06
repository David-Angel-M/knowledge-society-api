from django.urls import path
from .views import PostList, PostDetail, CategoryList, PostListProv, PostCreateProv, PostDetailProv, PostDeleteProv
from .views import PostCreate, PostDelete

urlpatterns = [
    path('posts-list/', PostList.as_view()),
    path('posts/', PostCreate.as_view()),
    path('posts/<id>/', PostDetail.as_view()),
    path('posts-delete/<id>/', PostDelete.as_view()),
    path('category-list/', CategoryList.as_view()),
    path('affiliate/posts-list/', PostListProv.as_view()),
    path('affiliate/posts/', PostCreateProv.as_view()),
    path('affiliate/posts/<id>/', PostDetailProv.as_view()),
    path('affiliate/posts-delete/<id>/', PostDeleteProv.as_view()),
]
