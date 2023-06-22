from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include(('App_login.urls'), namespace='App_login')),
    path('', include(('App_video.urls'), namespace='App_video')),
    path('activity/', include(('App_activity.urls'), namespace='App_activity')),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
