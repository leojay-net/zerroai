from rest_framework.response import Response
from rest_framework import status
from .serializers import CheckerSerializer
from rest_framework.generics import GenericAPIView
from .check import check





class CHECK(GenericAPIView):
    serializer_class = CheckerSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            result = check(check_text=str(serializer.data['text']))
            response = serializer.data
            response["response"] = result
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
