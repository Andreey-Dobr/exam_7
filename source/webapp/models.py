from django.db import models

class Poll(models.Model):
    poll = models.TextField(max_length=3000, null=False, verbose_name='вопрос')
    data =  models.DateTimeField(auto_now=True, verbose_name='Время создания')

    def __str__(self):
        return "{}. {}".format(self.pk, self.poll)


class Choice(models.Model):
    text = models.TextField(max_length=3000, null=False, verbose_name='ответ')
    poll = models.ForeignKey('webapp.Poll', related_name='pol', on_delete=models.CASCADE
                               , verbose_name='вопрос')

    def __str__(self):
        return "{}. {}".format(self.poll, self.text)
