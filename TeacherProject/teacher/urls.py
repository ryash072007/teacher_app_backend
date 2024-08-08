from django.urls import include, path
from .views import TeacherSignUpEndPoint, TeacherResetPasswordEndpoint,TeacherConfirmOTPEndPoint, TeacherSignInEndPoint, StudentAddEndPoint

urlpatterns = [
    path('signup/', TeacherSignUpEndPoint.as_view()),
    path('signin/', TeacherSignInEndPoint.as_view()),
    path('reset/email/', TeacherResetPasswordEndpoint.as_view()),
    path('reset/otp/', TeacherConfirmOTPEndPoint.as_view()),
    path('student/add/', StudentAddEndPoint.as_view())
]