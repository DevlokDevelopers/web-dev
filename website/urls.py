from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import*

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('services/', ServiceView.as_view(), name='services'),
    path('about/', AboutView.as_view(), name='about'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
