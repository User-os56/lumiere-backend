from django.contrib import admin
from .models import AssessmentResult
from .models import UserProgress
from .models import EmailVerification
from .models import UserProfile

admin.site.register(AssessmentResult)
admin.site.register(UserProgress)
admin.site.register(EmailVerification)
admin.site.register(UserProfile)