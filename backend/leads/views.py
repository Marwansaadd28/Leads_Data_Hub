from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Lead
from .serializers import LeadSerializer


class LeadListAPI(APIView):

    def filter_queryset(self, request, queryset):
        """
        Apply search and filtering.
        """

        search = request.query_params.get("search")
        status_filter = request.query_params.get("status")
        source = request.query_params.get("source")

        if search:
            queryset = queryset.filter(
                name__icontains=search
            )

        if status_filter:
            queryset = queryset.filter(
                status=status_filter
            )

        if source:
            queryset = queryset.filter(
                source__icontains=source
            )

        return queryset

    def get(self, request):

        leads = Lead.objects.all()

        leads = self.filter_queryset(
            request,
            leads
        )

        serializer = LeadSerializer(
            leads,
            many=True
        )

        return Response(serializer.data)

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
            Lead,
            pk=pk
        )

    def get(self, request, pk):

        lead = self.get_object(pk)

        serializer = LeadSerializer(lead)

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

        lead = self.get_object(pk)

        lead.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )