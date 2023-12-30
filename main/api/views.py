from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TextSerializer
from lib_managed_string.utils import capitalize_each_word
# Create your views here.

class CapitalizeTextView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TextSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data.get('text')
            capitalized_text = capitalize_each_word(text)
            return Response({'capitalized_text': capitalized_text})
        return Response(serializer.errors, status=400)