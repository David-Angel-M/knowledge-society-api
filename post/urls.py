from django.urls import path
from .views import PostListProv, PostCreate, PostDetailProv, PostDeleteProv

urlpatterns = [
    path('post-list/', PostListProv.as_view()),
    path('post/', PostCreate.as_view()),
    path('post/<id>/', PostDetailProv.as_view()),
    path('post-delete/<id>/', PostDeleteProv.as_view()),
]
