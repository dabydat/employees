from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # urls de departamento app
    re_path('', include('applications.department.urls')),
    re_path('', include('applications.employee.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
