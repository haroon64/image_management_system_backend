from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Image
from .serializers import ImageSerializer
from django.shortcuts import get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser


class ImageListCreateAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser) 

    def get(self, request):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Image uploaded successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ImageDeleteAPIView(APIView):

    def delete(self, request, pk):
        image = get_object_or_404(Image, pk=pk)
        image.delete()
        return Response({
            "message": "Image deleted successfully"
        }, status=status.HTTP_204_NO_CONTENT)