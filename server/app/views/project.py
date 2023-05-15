from django.http import JsonResponse
from django.views import View

from ..models.project import Project


class ProjectView(View):
    """View for a project."""

    def get(self, request):
        projects = Project.objects.values(
            "project_number",
            "client_name",
            "project_name",
            "site_address",
        )
        return JsonResponse(list(projects), safe=False)
