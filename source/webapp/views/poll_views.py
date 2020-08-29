from django.shortcuts import render
from django.views.generic import ListView
from webapp.models import Poll


class PollListView(ListView):
    model = Poll
    template_name = 'poll/poll_list.html'
    context_object_name = 'polls'


def index_view(request):
    polls = Poll.objects.all()
    context = {
        'polls': polls
    }
    return render(request, 'poll/poll_list.html', context)


