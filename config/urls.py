from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from config import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('employees/', include('employees.urls')),
    path('chatbot/', include('chatbot.urls')),
    path('recommend/', include('recommend.urls')),
    path('chart/', include('chart.urls')),
    path('', views.main, name='main')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)