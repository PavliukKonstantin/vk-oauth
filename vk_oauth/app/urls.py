from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='/app/login/', permanent=True)),
    path('login/', include('social_django.urls', namespace='social')),
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='login.html',
            redirect_authenticated_user=True,
        ),
        name='app_login',
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(template_name='logged_out.html'),
        name='app_logout',
    ),
    path('vk-friends/', views.index, name='index'),
]
