from rest_framework import serializers
from .models import Teacher, Student

class TeacherSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["email", "password", "phone", "name"]

class StudentAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"