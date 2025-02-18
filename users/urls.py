from django.urls import path
from .views import CustomUserCreate, BlacklistTokenUpdateView

urlpatterns = [
    path('register/', CustomUserCreate.as_view(), name='create-user'),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(), name='logout'),
]
