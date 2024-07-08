from rest_framework import generics
from rest_framework.permissions import (
    IsAdminUser, DjangoModelPermissionsOrAnonReadOnly,
    DjangoModelPermissions, BasePermission, IsAuthenticated
)
from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.permissions import SAFE_METHODS
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser

from blog.models import Post
from .serializers import PostSerializer

class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only.'
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user
        # return super().has_object_permission(request, view, obj)
    

# class PostList(generics.ListCreateAPIView):
#     permission_classes = [DjangoModelPermissions]
#     queryset = Post.post_objects.all()
#     serializer_class = BlogSerializer


# class PostDetails(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
#     permission_classes = [PostUserWritePermission]
#     queryset = Post.objects.all()
#     serializer_class = BlogSerializer
    
# class PostList(viewsets.ViewSet):
#     # permission_classes = [IsAuthenticated]
#     queryset = Post.post_objects.all()
    
#     def list(self, request):
#         serializer_class = PostSerializer(self.queryset, many=True)
#         return Response(serializer_class.data)
    
#     def retrieve(self, request, pk=None):
#         post = get_object_or_404(self.queryset, pk=pk)
#         serializer_class = PostSerializer(post)
#         return Response(serializer_class.data)

class PostList(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    # queryset = Post.post_objects.all()
    serializer_class = PostSerializer
    
    # define custom query
    def get_queryset(self):
        return Post.objects.all()
    
    def get_object(self):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)
    

class UserAvatarUpload(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    
    def post(self, request, format=None):
        print(request)
        serializer = PostSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    