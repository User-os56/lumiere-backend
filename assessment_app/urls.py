from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views 

urlpatterns = [
    #Authentication
    path('auth/send-code/', views.send_verification_code, name='send_verification_code'),
    path('auth/register/', views.register, name='register'),
    path('auth/login/', views.login_view, name='login'),
    path('auth/resend-code/', views.resend_code, name='resend_code'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #Assessments
    path('start-assessment/',  views.start_assessment, name='start_assessment'),
    path('process-answer/', views.process_answer, name='process_answer'),
    #Recommendations
    path('recommendations/', views.recommendations_api, name='recommendations'),
    path('profile/', views.profile_view, name='profile'),
]