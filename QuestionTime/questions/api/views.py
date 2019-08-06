from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 
from .serializers import QuestionSerializer
from .permissions import IsAuthorOrReadOnly
from questions.models import Question


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    lookup_field = 'slug'
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthorOrReadOnly, IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
