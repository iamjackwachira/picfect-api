from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls')),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include('rest_framework_docs.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
