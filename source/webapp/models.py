from django.db import models




class Poll(models.Model):
    text = models.TextField(max_length=3000, null=False, verbose_name='вопрос')
    data = models.DateTimeField(auto_now=True, verbose_name='Время создания')




class Choice(models.Model):
    text = models.TextField(max_length=3000, null=False, verbose_name='ответ')
    poll = models.ForeignKey('webapp.Poll', related_name='pol', on_delete=models.CASCADE,
                                verbose_name ='вопрос')

    def __str__(self):
        return "{}. {}".format(self.poll, self.text)

class Answer(models.Model):
    poll = models.ForeignKey('webapp.Poll', related_name='poll', on_delete=models.CASCADE,
                                verbose_name ='вопрос')
    data_time = models.DateTimeField(auto_now=True, verbose_name='Время создания')
    choice = models.ForeignKey('webapp.Choice', related_name='choice', on_delete=models.CASCADE,
                             verbose_name='ответ')



