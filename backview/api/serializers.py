from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Project, Contact, Testimonial, Consult, Question

class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['id', 'name', 'testimonial', 'profile_picture', 'approved']
        read_only_fields = ['approved']  # Prevent approval field modification by users

class ConsultSerializer(ModelSerializer):
    class Meta:
        model = Consult
        fields = '__all__'

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'