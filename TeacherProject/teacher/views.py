from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import TeacherSignUpSerializer
from .models import Teacher
from .otp import createOTP, sendOTP

# Create your views here.
class TeacherSignUpEndPoint(APIView):
    def post(self, request):
        print(request.data)
        if Teacher.objects.filter(email = request.data["email"]).exists():
            return Response({"message": "Teacher email already exists!", "status": 400})
        serializer = TeacherSignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Teacher created successfully", "status": 201})

class TeacherResetPasswordEndpoint(APIView):
    def post(self, request):
        if not Teacher.objects.filter(email = request.data["email"]).exists():
            return Response("Email is not a registered teacher", 400)
        
        # Accessing teacher
        teacher = Teacher.objects.get(email = request.data["email"])

        teacher.forgottenPassword = True
        teacher.otp = createOTP()
        teacher.save()

        if not sendOTP(teacher.email, teacher.otp):
            return Response("Failed to send OTP", 500)
        return Response("Otp Sent", 200)

class TeacherConfirmOTPEndPoint(APIView):
    def post(self, request):
        if not Teacher.objects.filter(email = request.data["email"]).exists():
            return Response("Email is not a registered teacher", 400)
        
        teacher = Teacher.objects.get(email = request.data["email"])

        if teacher.forgottenPassword == False:
            return Response("Teacher does not want to reset account", 401)

        if not (teacher.otp == request.data['otp']):
            return Response("Invalid OTP", 401)
        
        teacher.forgottenPassword = False
        teacher.password = request.data['password']
        teacher.save()

        return Response("Teacher password successfully changed", 201)

class TeacherSignInEndPoint(APIView):
    def post(self, request):
        if not Teacher.objects.filter(email = request.data["email"]).exists():
            return Response("Given email is not a registered teacher", 401)
        teacher = Teacher.objects.get(email = request.data["email"])            
        if not (request.data['password'] == teacher.password):
            return Response("Incorrect password", 401)
        return Response("Successfully signed in", 200)