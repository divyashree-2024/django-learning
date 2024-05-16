from rest_framework.viewsets import ViewSet
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from .serializers import QuestionSerializer
from .models import Question

class QuestionListView(ViewSet, ListAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def create(self, request):
        data = request.data
        if not data.get("question_text"):
            return Response(data={}, status=HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            instance = serializer.create(validated_data=serializer._validated_data)
        return Response(data=serializer.data, status=HTTP_201_CREATED)

    def delete(self, request,question_id):
        question = self.queryset.get(id=question_id)
        question.delete()
        return Response(data={}, status=HTTP_200_OK)