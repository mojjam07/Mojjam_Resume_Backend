from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProjectViewSet,
    ContactViewSet,
    ConsultViewSet,
    QuestionViewSet,
    ApprovedTestimonialListView,
    SubmitTestimonialView,
)

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'contacts', ContactViewSet, basename='contact')
router.register(r'consults', ConsultViewSet, basename='consult')
router.register(r'questions', QuestionViewSet, basename='question')
router.register(r'testimonials', QuestionViewSet, basename='testimonials')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/testimonials/approved/', ApprovedTestimonialListView.as_view(), name='approved_testimonials'),
    path('api/testimonials/submit/', SubmitTestimonialView.as_view(), name='submit_testimonial'),
]
