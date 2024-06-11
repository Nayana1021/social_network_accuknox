# api/views.py

from django.contrib.auth import authenticate, login
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CustomUser, FriendRequest
from .serializers import UserSerializer, FriendRequestSerializer
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from rest_framework.throttling import UserRateThrottle

class UserSignupView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

@api_view(['GET'])
def dummy_endpoint(request):
    """
    A dummy endpoint for testing purposes.
    """
    return Response({"message": "This is a dummy endpoint. It works!"})

@api_view(['POST'])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)

class UserSearchView(generics.ListAPIView):
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        return CustomUser.objects.filter(Q(email__iexact=query) | Q(username__icontains=query))

class FriendRequestThrottle(UserRateThrottle):
    rate = '3/minute'

class FriendRequestView(generics.CreateAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer
    throttle_classes = [FriendRequestThrottle]

    def perform_create(self, serializer):
        serializer.save(from_user=self.request.user)

@api_view(['POST'])
def respond_friend_request(request, request_id, response):
    try:
        friend_request = FriendRequest.objects.get(id=request_id, to_user=request.user)
        if response == 'accept':
            friend_request.status = 'accepted'
        elif response == 'reject':
            friend_request.status = 'rejected'
        friend_request.save()
        return Response({"message": "Friend request updated"}, status=status.HTTP_200_OK)
    except FriendRequest.DoesNotExist:
        return Response({"error": "Friend request not found"}, status=status.HTTP_404_NOT_FOUND)

class FriendsListView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        return CustomUser.objects.filter(Q(from_user__to_user=user, from_user__status='accepted') |
                                         Q(to_user__from_user=user, to_user__status='accepted'))

class PendingFriendRequestsView(generics.ListAPIView):
    serializer_class = FriendRequestSerializer

    def get_queryset(self):
        return FriendRequest.objects.filter(to_user=self.request.user, status='pending')
