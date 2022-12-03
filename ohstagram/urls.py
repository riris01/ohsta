from django.urls import path, include
from .views import Main, UploadFeed
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('content/upload', UploadFeed.as_view()),
    path('user/', include('user.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)