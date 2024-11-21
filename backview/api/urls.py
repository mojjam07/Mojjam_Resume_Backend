from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProjectViewSet,
    ContactViewSet,
    ConsultViewSet,
    QuestionViewSet,
    TestimonialListView
)

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'contacts', ContactViewSet, basename='contact')
router.register(r'consults', ConsultViewSet, basename='consult')
router.register(r'questions', QuestionViewSet, basename='question')
router.register(r'testimonials', TestimonialListView.as_view(), name='testimonials')

urlpatterns = [
    path('api/', include(router.urls)),
]
