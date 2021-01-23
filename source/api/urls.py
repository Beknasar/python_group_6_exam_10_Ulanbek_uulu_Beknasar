from django.urls import path
from api.views import FriendADDView, get_token_view, FriendRemoveView

app_name = 'api'

urlpatterns = [
    path('get-token/', get_token_view, name='get_token'),
    path('friend/<int:pk>/add/', FriendADDView.as_view(), name='friend_add'),
    path('friend/<int:pk>/remove/', FriendRemoveView.as_view(), name='friend_remove')
]

