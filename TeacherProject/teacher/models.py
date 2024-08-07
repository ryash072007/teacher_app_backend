from django.db import models

# Create your models here.
class Teacher(models.Model):

    # Main Details
    email = models.EmailField("Teacher Email Address", max_length=50)
    password = models.TextField("Teacher Password", max_length=20)
    phone = models.IntegerField("Teacher Phone no.", max_length=10)
    name = models.TextField("Teacher Name", max_length=30)

    # Supplementary Details
    qualifications = models.TextField("Teacher Qualifications", max_length=200)

    # OTP Details
    onboarded = models.BooleanField("Teacher Onboarded Status", default=False)
    forgottenPassword = models.BooleanField("Teacher Forgotten Password")
    otp = models.IntegerField("OTP Password", max_length=4)

