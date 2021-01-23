from django.urls import path, include
from webapp.views import IndexView, MailBox, MessageSendView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('mail/', MailBox.as_view(), name='mail'),
    path('<int:pk>/send_message/', MessageSendView.as_view(), name='send_mes'),
]

