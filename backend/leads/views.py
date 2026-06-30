from django.shortcuts import get_object_or_404
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Lead, Source, Status
from .serializers import (
    LeadSerializer,
    SourceSerializer,
    StatusSerializer,
)


class LeadListAPI(APIView):

    def filter_queryset(self, request, queryset):

        search = request.query_params.get("search")
        source = request.query_params.get("source")
        status_filter = request.query_params.get("status")

        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) |
                Q(email__icontains=search)
            )

        if source:
            queryset = queryset.filter(
                source__name__iexact=source
            )

        if status_filter:
            queryset = queryset.filter(
                status__name__iexact=status_filter
            )

        return queryset

    def paginate_queryset(self, request, queryset):

        page = int(request.query_params.get("page", 1))
        page_size = int(request.query_params.get("page_size", 20))

        start = (page - 1) * page_size
        end = start + page_size

        total = queryset.count()

        return {
            "count": total,
            "page": page,
            "page_size": page_size,
            "total_pages": (total + page_size - 1) // page_size,
            "results": queryset[start:end],
        }
    
    def get(self, request):

        leads = Lead.objects.select_related(
            "source",
            "status"
        )

        leads = self.filter_queryset(
            request,
            leads
        )

        paginated = self.paginate_queryset(
            request,
            leads
        )

        serializer = LeadSerializer(
            paginated["results"],
            many=True
        )

        return Response({
            "count": paginated["count"],
            "page": paginated["page"],
            "page_size": paginated["page_size"],
            "total_pages": paginated["total_pages"],
            "results": serializer.data,
        })

    def post(self, request):

        serializer = LeadSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class LeadDetailAPI(APIView):

    def get_object(self, pk):
        return get_object_or_404(
            Lead.objects.select_related(
                "source",
                "status"
            ),
            pk=pk
        )

    def get(self, request, pk):

        serializer = LeadSerializer(
            self.get_object(pk)
        )

        return Response(serializer.data)

    def patch(self, request, pk):

        lead = self.get_object(pk)

        serializer = LeadSerializer(
            lead,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):

        self.get_object(pk).delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )


class SourceListAPI(APIView):

    def get(self, request):

        serializer = SourceSerializer(
            Source.objects.all(),
            many=True
        )

        return Response(serializer.data)


class StatusListAPI(APIView):

    def get(self, request):

        serializer = StatusSerializer(
            Status.objects.all(),
            many=True
        )

        return Response(serializer.data)