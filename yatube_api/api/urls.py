from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .views import PostViewSet, GroupViewSet, CommentViewSet


first_router = DefaultRouter()
first_router.register('posts', PostViewSet, basename='posts')
first_router.register('groups', GroupViewSet, basename='groups')
first_router.register(
    r'posts/(?P<post_id>.+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('v1/', include(first_router.urls)),
]
