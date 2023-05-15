from django.http import JsonResponse
from django.views import View

from ..models.log import Log


class LogView(View):
    """View for a log."""

    def get(self, request, borehole_id):
        """Handles a `get` request."""
        logs = Log.objects.filter(borehole_id=borehole_id).values(
            "depth",
            "soil_type",
            "description",
            "sample_number",
            "sample_type",
            "spt_count",
        )
        return JsonResponse(list(logs), safe=False)
