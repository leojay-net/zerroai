from rest_framework import serializers



class CheckerSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=1000000)
    