from rest_framework import serializers

from shortner.models import URL

class URLSerializer(serializers.Serializer):
    original_url = serializers.URLField()

    def create(self, validated_data):
        # # Dedup logic (important improvement)
        existing = URL.objects.filter(
            original_url=validated_data['original_url']
        ).first()

        if existing:
            return existing

        # Create without short_code (your view handles it)
        return URL.objects.create(**validated_data)
    

class URLAnalyticsSerializer(serializers.Serializer):
    total_clicks = serializers.IntegerField()
    class Meta:
        model = URL
        fields = [
            "original_url",
            "short_code",
            "created_at",
            "total_clicks",
        ]