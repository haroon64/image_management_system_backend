from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'images'

urlpatterns = [
    path('upload/', views.UploadImageAPIView.as_view(), name='image-upload'),
    path('', views.ImageListAPIView.as_view(), name='image-list'),
    path('delete/<int:pk>/', views.ImageDeleteAPIView.as_view(), name='image-delete'),

    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)