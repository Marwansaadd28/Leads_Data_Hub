from rest_framework import serializers
from .models import Lead, Source, Status


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = "__all__"


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"


class LeadSerializer(serializers.ModelSerializer):
    source = SourceSerializer(read_only=True)
    status = StatusSerializer(read_only=True)

    source_id = serializers.PrimaryKeyRelatedField(
        queryset=Source.objects.all(),
        source="source",
        write_only=True,
    )

    status_id = serializers.PrimaryKeyRelatedField(
        queryset=Status.objects.all(),
        source="status",
        write_only=True,
    )

    class Meta:
        model = Lead
        fields = [
            "id",
            "lead_id",
            "name",
            "email",
            "phone",
            "created_at",
            "source",
            "status",
            "source_id",
            "status_id",
        ]