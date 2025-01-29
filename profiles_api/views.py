from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import HelloSerializer

class HelloApiView(APIView):
    """Test API View"""

    serializer_class = HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        features = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]

        return Response({ 'message': 'Hello!', 'features': features })
    
    def post(self, request):
        """Create a hello message with name from the request"""
        serializer = self.serializer_class(data=request.data)

        # Is valid if request contains required fields and additional fields
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        name = serializer.validated_data.get('name')
        return Response({ 'message': f'Hello {name}'})