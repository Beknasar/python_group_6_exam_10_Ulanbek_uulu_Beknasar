from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, \
    UserPassesTestMixin
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseForbidden

from django.db.models import Q
from django.urls import reverse

from django.utils.timezone import make_naive
from django.views.generic import View, DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import SearchForm
from django.contrib.auth.models import User
from accounts.models import Relationship, Profile
from .base_views import SearchView


class IndexView(SearchView):
    template_name = 'index.html'
    context_object_name = 'users'
    paginate_by = 10
    paginate_orphans = 0
    model = User
    ordering = ['first_name']
    search_fields = ['first_name__icontains', 'last_name__icontains']

    def get_queryset(self):
        data = User.objects.all()
        form = SearchForm(data=self.request.GET)
        if form.is_valid():
            search = form.cleaned_data['search']
            if search:
                data = data.filter(Q(name__icontains=search) | Q(description__icontains=search))
        return data


