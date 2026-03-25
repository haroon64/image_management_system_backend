from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import RegisterSerializer

class RegisterView(APIView):
    # Allow anyone to hit this endpoint to create an account
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        print(request.data )
        serializer = RegisterSerializer(data=request.data['user'])
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User created successfully"}, 
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)