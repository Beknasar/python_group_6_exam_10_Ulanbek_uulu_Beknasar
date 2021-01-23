import json

from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.views import APIView

from accounts.models import Profile


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')


class FriendADDView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['pk'])
        if user:
            request.user.profile.relationships.add(user.profile)
            return HttpResponse("Added")
        else:
            HttpResponseNotFound()


class FriendRemoveView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['pk'])
        if user:
            request.user.profile.relationships.remove(user.profile)
            return HttpResponse('Deleted')
        else:
            return HttpResponseNotFound()
