# posts/serializers.py
from rest_framework import serializers

from .models import Post

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "author",
            "title",
            "body",
            "creation_at",
        )
        model = Post