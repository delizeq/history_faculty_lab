from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("faculty.urls")),
    path("", include("exchange.urls")),
]
