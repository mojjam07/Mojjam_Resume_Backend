from rest_framework.serializers import ModelSerializer
from .models import Project, Profile, Skill, Education, Experience, Contact, Testimonial, NewTestimonial, Service, Consult, Question

class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class SkillSerializer(ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class EducationSerializer(ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class ExperienceSerializer(ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class TestimonialSerializer(ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'

class NewTestimonialSerializer(ModelSerializer):
    class Meta:
        model = NewTestimonial
        fields = '__all__'

class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class ConsultSerializer(ModelSerializer):
    class Meta:
        model = Consult
        fields = '__all__'

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'