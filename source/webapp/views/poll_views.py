
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from webapp.forms import PollForm
from webapp.models import Poll


class PollListView(ListView):
    model = Poll
    template_name = 'poll/poll_list.html'
    context_object_name = 'polls'
    ordering = ['-data']
    paginate_by = 5



class PollViews(DetailView):
    template_name = 'poll/poll_view.html'
    model = Poll

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context




class PollCreate(CreateView):
    template_name = 'poll/poll_create.html'
    form_class = PollForm
    model = Poll

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})

class Poll_Update(UpdateView):
    model = Poll
    template_name = 'poll/poll_update.html'
    form_class = PollForm
    context_object_name = 'poll'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})

class Delete_Poll(DeleteView):
    template_name = 'poll/poll_delete.html'
    model = Poll
    context_key = 'poll'

    def get_success_url(self):
        return reverse('poll_list')


