from django.urls import include, path
from .views import TeacherSignUpEndPoint, TeacherResetPasswordEndpoint,TeacherConfirmOTPEndPoint, TeacherSignInEndPoint

urlpatterns = [
    path('signup/', TeacherSignUpEndPoint.as_view()),
    path('signin/', TeacherSignInEndPoint.as_view()),
    path('reset/email/', TeacherResetPasswordEndpoint.as_view()),
    path('reset/otp/', TeacherConfirmOTPEndPoint.as_view())
]