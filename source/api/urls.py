from django.urls import path
from api.views import FriendADDView, get_token_view

app_name = 'api'

urlpatterns = [
    path('friend/<int:pk>/add/', FriendADDView.as_view(), name= 'friend_add'),
    path('get-token/', get_token_view, name='get_token')
]

