from django.views.generic import ListView, DetailView

from webapp.models import Answer


class AnswerListView(ListView):
    model = Answer
    template_name = 'answer/answer_list.html'
    context_object_name = 'answers'

#    paginate_by = 5

    def get_queryset(self):

        return Answer.objects.all().order_by('-poll')


class AnswerViews(DetailView):
    template_name = 'answer/answer_view.html'
    model = Answer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context