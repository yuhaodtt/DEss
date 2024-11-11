from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def query_data(request):
    query = request.data.get("query")
    # Process query, connect to data sources, and return data
    data = {"message": "Data retrieved based on your query"}
    return Response(data)