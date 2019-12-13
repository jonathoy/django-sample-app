from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mentor_finder.urls', namespace='mentor_finder'))
]
