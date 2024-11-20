
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from rest_framework.schemas import get_schema_view
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('app/', include('app.urls')),
    path('store/', include('store.urls')),
    path('api_schema/', get_schema_view(
        title='API Schema',
        description='Guide for the REST API'
    ), name='api_schema'),
    path('docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url':'api_schema'}
        ), name='swagger-ui'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
