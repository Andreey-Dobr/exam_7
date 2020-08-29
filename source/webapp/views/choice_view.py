from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView, UpdateView, CreateView, DeleteView

from webapp.forms import ChoiceForm
from webapp.models import Choice, Poll


class Choice_View(TemplateView):
    template_name = 'choice/choice_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        choice = get_object_or_404(Choice, pk=pk)
        context['choice'] = choice
        return context

class Choice_Create(CreateView):
    template_name = 'choice/choice_creat.html'
    form_class = ChoiceForm
    model = Choice

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        choice = form.save(commit=False)
        choice.poll = poll
        choice.save()
        return redirect('poll_view', pk=poll.pk)


class Choice_Update_View(UpdateView):
    model = Choice
    template_name = 'choice/choice_update.html'
    form_class = ChoiceForm


    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll.pk})



class Delete_Choice(DeleteView):
    model = Choice
    template_name = "choice/choice_delete.html"
    context_key = 'poll'


    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll.pk})


class Delete_Poll(DeleteView):
    template_name = 'poll/poll_delete.html'
    model = Poll
    context_key = 'poll'

    def get_success_url(self):
        return reverse('poll_list')