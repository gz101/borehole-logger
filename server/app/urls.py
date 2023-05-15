from django.urls import path
from .views import (
    ProjectView,
    BoreholeView,
    LogView,
)


url_patterns = [
    path("projects/", ProjectView.as_view(), name="projects"),
    path(
        "projects/<int:project_id>/boreholes/",
        BoreholeView.as_view(),
        name="boreholes",
    ),
    path(
        "projects/<int:project_id>/boreholes/<int:borehole_id>/logs",
        LogView.as_view(),
        name="logs",
    ),
]
