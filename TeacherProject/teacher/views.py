from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import TeacherSignUpSerializer, StudentAddSerializer, TeacherQualificationSerializer
from .models import Teacher, Student
from .otp import createOTP, sendOTP

# Create your views here.
class TeacherSignUpEndPoint(APIView):
    def post(self, request):
        print(request.data)
        if Teacher.objects.filter(email = request.data["email"]).exists():
            return Response({"message": "Teacher email already exists!", "status": 400}, 400)
        serializer = TeacherSignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Teacher created successfully", "status": 201}, 201)

class TeacherQualificationEndPoint(APIView):
    def post(self, request):
        serializer = TeacherQualificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Teacher Qualification added", "status": 201}, 201)
        return Response({"message": "Invalid Qualification Request", "status": 400}, 400)

class TeacherResetPasswordEndpoint(APIView):
    def post(self, request):
        if not Teacher.objects.filter(email = request.data["email"]).exists():
            return Response({"message": "Email is not a registered teacher", "status": 400}, 400)
        
        # Accessing teacher
        teacher = Teacher.objects.get(email = request.data["email"])

        teacher.forgottenPassword = True
        teacher.otp = createOTP()
        teacher.save()

        if not sendOTP(teacher.email, teacher.otp):
            return Response({"message": "Failed to send OTP", "status": 500}, 500)
        return Response({"message": "OTP Sent", "status": 200}, 200)

class TeacherConfirmOTPEndPoint(APIView):
    def post(self, request):
        if not Teacher.objects.filter(email = request.data["email"]).exists():
            return Response({"message": "Email is not a registered teacher", "status": 400}, 400)
        
        teacher = Teacher.objects.get(email = request.data["email"])

        if teacher.forgottenPassword == False:
            return Response({"message": "Teacher does not want to reset account", "status": 401}, 401)

        if not (teacher.otp == request.data['otp']):
            return Response({"message": "Invalid OTP", "status": 401}, 401)
        
        teacher.forgottenPassword = False
        teacher.password = request.data['password']
        teacher.save()

        return Response({"message": "Teacher password successfully changed", "status": 201}, 201)

class TeacherSignInEndPoint(APIView):
    def post(self, request):
        if not Teacher.objects.filter(email = request.data["email"]).exists():
            return Response({"message": "Given email is not a registered teacher", "status": 401}, 401)
        teacher = Teacher.objects.get(email = request.data["email"])            
        if not (request.data['password'] == teacher.password):
            return Response({"message": "Incorrect password", "status": 401}, 401)
        return Response({"message": "Successfully signed in", "status": 200}, 200)

class StudentAddEndPoint(APIView):
    def post(self, request):
        serializer = StudentAddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Student Added", "status": 200}, 200)
        return Response({"message": "Invalid Request", "status": 400}, 400)

class StudentRemoveEndPoint(APIView):
    def post(self, request):
        print([obj.id for obj in Student.objects.all()])
        if not Student.objects.filter(id=request.data["id"]).exists():
            return Response({"message": "Invalid Student ID", "status": 400}, 400)
            
        student = Student.objects.get(id=request.data["id"])
        student.delete()

        return Response({"message": "Student deleted successfully", "status": 200}, 200)

class StudentsListEndPoint(APIView):
    def post(self, request):
        studentList = Student.objects.filter(teacher=request.data["email"])
        responseList = [
            {
                "firstName": student.firstName,
                "lastName": student.lastName,
                "displayImage": request.build_absolute_uri(student.displayImage.url) if student.displayImage else None,
                "grade": student.grade,
                "id": student.id
            } for student in studentList
        ]
        return Response({"data": responseList, "status": 201}, 201)

class StudentDetailsEndPoint(APIView):
    def post(self, request):
        if not Student.objects.filter(id=request.data["id"]).exists():
            return Response({"message": "Invalid Student ID", "status": 400}, 400)
        student = Student.objects.get(id=request.data["id"])
        responseJSON = {
            "firstName": student.firstName,
            "lastName": student.lastName,
            "gender": student.gender,
            "grade": student.grade,
            "studentDesc": student.studentDesc,
            "displayImage": request.build_absolute_uri(student.displayImage.url) if student.displayImage else None,
            "parentName": student.parentName,
            "parentEmail": student.parentEmail,
            "id": student.id
        }
        return Response({"data": responseJSON, "status": 201}, 201)
