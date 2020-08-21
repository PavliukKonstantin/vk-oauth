# from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(url='/app/', permanent=True)),
    path('app/', include('app.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('admin/', admin.site.urls),
]
