import json
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView

from accounts.models import Profile


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')


class FriendADDView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        user_profile = get_object_or_404(Profile)
        if request.user.profile not in user_profile.relationships.all():
            user_profile.relationships.add(request.user.profile)
            return HttpResponse("ADDED")
        else:
            return HttpResponseNotAllowed()