from django.urls import path

from .views import (
    LeadListAPI,
    LeadDetailAPI,
    SourceListAPI,
    StatusListAPI,
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

    path(
        "sources/",
        SourceListAPI.as_view(),
        name="source-list",
    ),

    path(
        "statuses/",
        StatusListAPI.as_view(),
        name="status-list",
    ),
]