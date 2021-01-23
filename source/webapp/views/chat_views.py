from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.urls import reverse

from django.views.generic import View, DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import SearchForm
from django.contrib.auth.models import User
from .base_views import SearchView
from webapp.forms import MessageForm
from webapp.models import Messages


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
                data = data.filter(Q(first_name__icontains=search) | Q(last_name__icontains=search))
        return data


class MessageSendView(CreateView):
    template_name = 'chat/sending_message.html'
    form_class = MessageForm
    model = Messages
    permission_required = 'webapp.add_project'

    def form_valid(self, form, **kwargs):
        message = form.save(commit=False)
        user = get_object_or_404(User, pk=self.kwargs.get('pk'))
        message.from_user =self.request.user.profile
        message.to_user = user.profile
        # form.save()
        form.save_m2m()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:mail')


class MailBox(DetailView):
    template_name = 'chat/chat.html'
    model = Messages
    paginate_tasks_by = 5
    paginate_tasks_orphans = 0

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        other_user = get_object_or_404(User, pk=kwargs['pk'])
        sent_messages = Messages.objects.filter(from_user=self.request.user.profile, to_user=other_user.profile)
        received_messages = Messages.objects.filter(to_user=self.request.user.profile, from_user=other_user.profile)
        context['sent_messages'] = sent_messages
        context['received_messages'] = received_messages
        # context['is_paginated'] = is_paginated
        return context



