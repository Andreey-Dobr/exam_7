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

from webapp.views import PollListView, PollCreate, PollViews, Poll_Update, Delete_Poll

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PollListView.as_view(), name='poll_list'),
    path('<int:pk>/', PollViews.as_view(), name='poll_view'),
    path('add/', PollCreate.as_view(), name='poll_create'),
    path('<int:pk>/edit/', Poll_Update.as_view(), name='poll_update'),
    path('<int:pk>/del/', Delete_Poll.as_view(), name='poll_delete'),

]
