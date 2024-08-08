from django.db import models

# Create your models here.
class Teacher(models.Model):

    # Main Details
    email = models.EmailField("Teacher Email Address", max_length=50, unique=True)
    password = models.TextField("Teacher Password", max_length=20)
    phone = models.TextField("Teacher Phone no.", max_length=10)
    name = models.TextField("Teacher Name", max_length=30)

    # Supplementary Details
    qualifications = models.TextField("Teacher Qualifications", max_length=200, blank=True)

    # OTP Details
    forgottenPassword = models.BooleanField("Teacher Forgotten Password", default=False)
    otp = models.TextField("OTP Password", max_length=4, null=True)

    # Student Details
    # studentList = models.Field

    def __str__(self):
        return self.name


def displayImageFilePath(instance, filename):
    return f"{instance.id}." + filename.split('.')[-1]


class Student(models.Model):

    class Gender(models.TextChoices):
        male = "male"
        female = "female"


    # Main Details
    firstName = models.TextField("Student First Name", max_length=30)
    lastName = models.TextField("Student Last Name", max_length=30)
    gender = models.TextField("Student Gender", choices=Gender.choices)
    grade = models.IntegerField("Student Grade")
    studentDesc = models.TextField("Student Description", max_length=200, blank=True)
    displayImage = models.ImageField("Student Display Image", null=True, blank=True, upload_to=displayImageFilePath)

    # Parent Details
    parentName = models.TextField("Parents Name", max_length=30)
    parentEmail = models.EmailField("Parents Email Address", max_length=50)

    # Teacher Linked
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstName
