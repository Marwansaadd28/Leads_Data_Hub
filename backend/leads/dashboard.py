from django.db.models import Count

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Lead, Source, Status


class DashboardAPI(APIView):

    def get(self, request):

        total_leads = Lead.objects.count()
        total_sources = Source.objects.count()
        total_statuses = Status.objects.count()

        leads_by_status = (
            Status.objects
            .annotate(count=Count("leads"))
            .values("name", "count")
        )

        leads_by_source = (
            Source.objects
            .annotate(count=Count("leads"))
            .values("name", "count")
        )

        recent_leads = (
            Lead.objects
            .select_related(
                "source",
                "status"
            )
            .order_by("-created_at")[:5]
        )

        recent = []

        for lead in recent_leads:

            recent.append({
                "lead_id": lead.lead_id,
                "name": lead.name,
                "email": lead.email,
                "source": lead.source.name,
                "status": lead.status.name,
                "created_at": lead.created_at,
            })

        return Response({

            "summary": {

                "total_leads": total_leads,
                "total_sources": total_sources,
                "total_statuses": total_statuses,

            },

            "leads_by_status": leads_by_status,

            "leads_by_source": leads_by_source,

            "recent_leads": recent,

        })