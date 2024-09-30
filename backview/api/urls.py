from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, SkillViewSet, ExperienceViewSet, EducationViewSet, ContactViewSet, ProfileViewSet, TestimonialViewSet, NewTestimonialViewSet, ServiceViewSet, ConsultViewSet, QuestionViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'skills', SkillViewSet )
router.register(r'experience', ExperienceViewSet)
router.register(r'education', EducationViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'profile', ProfileViewSet)
router.register(r'testimonials', TestimonialViewSet)
router.register(r'newtestimonials', NewTestimonialViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'consults', ConsultViewSet)
router.register(r'questions', QuestionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]