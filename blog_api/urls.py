from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostList #, PostDetails

app_name = 'blog_api'

# urlpatterns = [
#     path('<int:pk>/', PostDetails.as_view(), name='detailed-create'),
#     path('', PostList.as_view(), name='list-create'),
# ]

router = DefaultRouter()
router.register('', PostList, basename='post')
urlpatterns = router.urls

