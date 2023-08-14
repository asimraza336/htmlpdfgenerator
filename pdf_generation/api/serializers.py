from rest_framework import serializers
# from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class GerneratePdfSerializer(serializers.Serializer):
    
    html_string = serializers.CharField(required=True)
    context = serializers.DictField(child=serializers.CharField(), required=False, default=None)
        
        