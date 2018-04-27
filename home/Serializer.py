from rest_framework import serializers

from home.models import Contact, Position


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields='__all__'