from django.urls import include, path

from .views import TeacherSignUpEndPoint,\
                    TeacherResetPasswordEndpoint,\
                    TeacherConfirmOTPEndPoint,\
                    TeacherSignInEndPoint,\
                    TeacherQualificationEndPoint,\
                    StudentAddEndPoint,\
                    StudentRemoveEndPoint,\
                    StudentsListEndPoint,\
                    StudentDetailsEndPoint
urlpatterns = [
    path('signup/', TeacherSignUpEndPoint.as_view()),
    path('signin/', TeacherSignInEndPoint.as_view()),
    path('qualifications/', TeacherQualificationEndPoint.as_view()),
    path('reset/email/', TeacherResetPasswordEndpoint.as_view()),
    path('reset/otp/', TeacherConfirmOTPEndPoint.as_view()),
    path('student/add/', StudentAddEndPoint.as_view()),
    path('student/remove/', StudentRemoveEndPoint.as_view()),
    path('student/list/', StudentsListEndPoint.as_view()),
    path('student/details/', StudentDetailsEndPoint.as_view()),
]