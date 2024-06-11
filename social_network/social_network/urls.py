# social_network/urls.py

from django.contrib import admin
from django.urls import path, include
from api.views import UserSignupView, login_view, UserSearchView, FriendRequestView, respond_friend_request, FriendsListView, PendingFriendRequestsView, dummy_endpoint

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/signup/', UserSignupView.as_view(), name='signup'),
    path('api/login/', login_view, name='login'),
    path('api/search/', UserSearchView.as_view(), name='search'),
    path('api/friend-request/', FriendRequestView.as_view(), name='friend_request'),
    path('api/friend-request/<int:request_id>/<str:response>/', respond_friend_request, name='respond_friend_request'),
    path('api/friends/', FriendsListView.as_view(), name='friends_list'),
    path('api/pending-requests/', PendingFriendRequestsView.as_view(), name='pending_requests'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/dummy/', dummy_endpoint, name='dummy_endpoint'),
]
