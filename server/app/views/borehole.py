from django.http import JsonResponse
from django.views import View

from ..models.borehole import Borehole


class BoreholeView(View):
    """View for a borehole."""

    def get(self, request, project_id):
        """Handles a `get` request."""
        boreholes = Borehole.objects.filter(project_id=project_id).values(
            "id",
            "borehole_number",
            "conducted_by",
            "date_logged",
            "groundwater_depth",
            "elevation",
            "drill_rig",
            "diameter",
            "total_boring_depth",
            "surface_description",
        )
        return JsonResponse(list(boreholes), safe=False)
