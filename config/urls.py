from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    re_path(r'^jet/', include(('jet.urls', 'jet'))),
    re_path(r'^jet/dashboard/', include('jet.dashboard.urls', namespace='jet-dashboard')),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]
