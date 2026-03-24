from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'images'

urlpatterns = [
    path('', views.ImageListCreateAPIView.as_view(), name='image-list-create'),
    path('<int:pk>/', views.ImageDeleteAPIView.as_view(), name='image-delete'),

    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)