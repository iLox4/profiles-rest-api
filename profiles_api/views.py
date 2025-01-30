from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.viewsets import ViewSet
from rest_framework import status

from .serializers import HelloSerializer

class HelloApiView(APIView):
    """Test API View"""

    serializer_class = HelloSerializer

    def get(self, request: Request, format=None):
        """Returns a list of APIView features"""
        features = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]

        return Response({ 'message': 'Hello!', 'features': features })
    
    def post(self, request: Request):
        """Create a hello message with name from the request"""
        serializer = self.serializer_class(data=request.data)

        # Is valid if request contains required fields and additional fields
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        name = serializer.validated_data.get('name')
        return Response({ 'message': f'Hello {name}' })
    

class HelloViewSet(ViewSet):
    """Test API ViewSet"""

    serializer_class = HelloSerializer

    def list(self, request: Request):
        """Return a list of ViewSet features"""
        features = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'
        ]

        return Response({ 'message': 'Hello!', 'features': features })
    
    def create(self, request: Request):
        """Create a hello message with name from the request"""
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        name = serializer.validated_data.get('name')
        return Response({ 'message': f'Hello {name}' })
    
    def retrieve(self, request: Request, pk=None):
        """Handle getting an object by ID(pk)"""
        return Response({'http_method': 'GET'})
    
    def update(self, request: Request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})
    
    def partial_update(self, request: Request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method': 'PATCH'})
    
    def destroy(self, request: Request, pk=None):
        """Handle deleting an object"""
        return Response({'http_method': 'DELETE'})