from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='/app/vk-friends/', permanent=True)),
    path('vk-friends/', views.index, name='index'),
]
