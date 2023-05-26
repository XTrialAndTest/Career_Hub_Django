from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from C_H_App.views import Jobviewsets, Company_viewsets
# (
#     ApplicantSignupView,
#     EmployerSignupView,
#     CustomAuthToken,
#     LogoutView,
#     ApplicantOnlyView,
#     EmployerOnlyView,
# )
router = DefaultRouter()
router.register(r'jobs', Jobviewsets, basename='job')
router.register(r'company', Company_viewsets, basename='company')
urlpatterns = router.urls

urlpatterns = [
    path('signup/applicant/', ApplicantSignupView.as_view(),
         name='applicant-signup'),
    path('signup/employer/', EmployerSignupView.as_view(), name='employer-signup'),
    path('login/', CustomAuthToken.as_view(), name='auth-token'),
    path('logout/', LogoutView.as_view(), name='logout-view'),
    path('applicant/page/', ApplicantOnlyView.as_view(), name='applicant-page'),
    path('employer/page/', EmployerOnlyView.as_view(), name='employer-page'),
    path('mine', include(router.urls)),
]
