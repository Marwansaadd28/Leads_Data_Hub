from django.urls import path

from .views import (
    LeadListAPI,
    LeadDetailAPI,
)

urlpatterns = [
    path(
        "",
        LeadListAPI.as_view(),
        name="lead-list",
    ),

    path(
        "<int:pk>/",
        LeadDetailAPI.as_view(),
        name="lead-detail",
    ),
]