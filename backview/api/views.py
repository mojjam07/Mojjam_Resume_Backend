from rest_framework.viewsets import ModelViewSet
from .models import Project, Skill, Experience, Education, Contact, Profile, Testimonial, NewTestimonial, Service, Consult, Question
from .serializers import ProjectSerializer, SkillSerializer, ExperienceSerializer, EducationSerializer, ContactSerializer, ProfileSerializer, TestimonialSerializer, NewTestimonialSerializer, ServiceSerializer, ConsultSerializer, QuestionSerializer

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class SkillViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class ExperienceViewSet(ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class EducationViewSet(ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class TestimonialViewSet(ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class NewTestimonialViewSet(ModelViewSet):
    queryset = NewTestimonial.objects.all()
    serializer_class = NewTestimonialSerializer

class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ConsultViewSet(ModelViewSet):
    queryset = Consult.objects.all()
    serializer_class = ConsultSerializer

class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer