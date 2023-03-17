from rest_framework import serializers


class ParserSerializer(serializers.Serializer):
    result = serializers.ListField()
