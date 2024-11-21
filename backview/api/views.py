from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from .models import Project, Contact, Testimonial, Consult, Question
from .serializers import ProjectSerializer, ContactSerializer, TestimonialSerializer, ConsultSerializer, QuestionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to Mojjam Resume Backend API!"})

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        # Optional: Limit query logic or provide filtered data
        return super().get_queryset()


# class ApprovedTestimonialListView(ListAPIView):
#     queryset = Testimonial.objects.filter(approved=True).only('name', 'testimonial', 'profile_picture')
#     serializer_class = TestimonialSerializer


# class SubmitTestimonialView(APIView):
#     parser_classes = (MultiPartParser, FormParser)

#     def post(self, request, *args, **kwargs):
#         try:
#             serializer = TestimonialSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save(approved=False)  # Default to not approved
#                 return Response(
#                     {"success": "Testimonial submitted and awaiting approval."},
#                     status=status.HTTP_201_CREATED,
#                 )
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TestimonialListView(APIView):
    def get(self, request):
        approved_testimonials = Testimonial.objects.filter(approved=True)
        serializer = TestimonialSerializer(approved_testimonials, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ConsultViewSet(ModelViewSet):
    queryset = Consult.objects.all()
    serializer_class = ConsultSerializer

class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer