from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404

from .models import Document
from .serializers import DocumentSerializer


class LoginView(APIView):
    def post(self, request, user_id):
        user = User.objects.get(pk=user_id)
        if not user:
            return Response({'error': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        # create token and return
        else:
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }, status=status.HTTP_200_OK)


class DocumentViewSet(viewsets.ViewSet):

    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = Document.objects.all()

        # Filter by tag ID
        tag_id = request.query_params.get('tag')
        if tag_id:
            queryset = queryset.filter(tags__id=tag_id)

        # Sort by created or updated
        sort_by = request.query_params.get('sort')
        if sort_by in ['created', 'updated']:
            queryset = queryset.order_by(sort_by)

        serializer = DocumentSerializer(queryset, many=True)
        return Response({'documents': serializer.data})

    def retrieve(self, request, pk=None):
        document = get_object_or_404(Document, pk=pk)
        serializer = DocumentSerializer(document)
        return Response({'document': serializer.data})

    def destroy(self, request, pk=None):
        document = get_object_or_404(Document, pk=pk)
        document.delete()
        return Response({'message': 'Document deleted'}, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        document = get_object_or_404(Document, pk=pk)
        serializer = DocumentSerializer(document, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'document': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'document': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
