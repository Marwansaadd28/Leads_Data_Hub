from django.urls import path
from .dashboard import DashboardAPI

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

    path(
        "dashboard/",
        DashboardAPI.as_view(),
        name="dashboard",
    ),
]