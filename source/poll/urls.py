"""poll URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from webapp.views import PollListView, PollCreate, PollViews, Poll_Update, Delete_Poll, \
    Choice_View, Choice_Update_View, Choice_Create, Delete_Choice, AnswerListView, AnswerViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PollListView.as_view(), name='poll_list'),
    path('poll/<int:pk>/', PollViews.as_view(), name='poll_view'),
    path('poll/add/', PollCreate.as_view(), name='poll_create'),
    path('poll/<int:pk>/update/', Poll_Update.as_view(), name='poll_update'),
    path('poll/<int:pk>/delete/', Delete_Poll.as_view(), name='poll_delete'),


    path('choise/<int:pk>', Choice_View.as_view(), name='choice_view'),
    path('poll/<int:pk>/choise/add', Choice_Create.as_view(), name='choice_create'),
    path('choice/<int:pk>/update/', Choice_Update_View.as_view(), name='choice_update'),
    path('choice/<int:pk>/delet_choice/', Delete_Choice.as_view(), name='del_choice'),


    path('answer/', AnswerListView.as_view(), name='answer'),
    path('poll/<int:pk>/answer/', AnswerViews.as_view(), name='answer_test'),
]
