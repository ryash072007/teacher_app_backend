from rest_framework import serializers
from .models import Teacher

class TeacherSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["email", "password", "phone", "name"]
