
# Serving media and static files during development
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

"""
urlpatterns = [
    # your urls
    """ 
    example:
    path('', home, name='home'),
    path('about/', about, name="about"),
    path('contact/', contact, name='contact'),
    """
]
"""
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

urlpatterns += staticfiles_urlpatterns()
