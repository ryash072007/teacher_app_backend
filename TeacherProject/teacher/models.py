from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import random
import string

class TeacherManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        print('createuser called')
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)

        return self.create_user(email, password, **extra_fields)

class Teacher(AbstractBaseUser, PermissionsMixin):
    # Main Details
    email = models.EmailField("Teacher Email Address", max_length=50, unique=True)
    password = models.CharField("Teacher Password", max_length=128)
    phone = models.CharField("Teacher Phone no.", max_length=13)
    name = models.CharField("Teacher Name", max_length=30)
    id = models.CharField("Teacher ID", max_length=6, unique=True, primary_key=True)
    # Supplementary Details
    qualifications = models.TextField("Teacher Qualifications", max_length=200, blank=True)

    # OTP Details
    forgottenPassword = models.BooleanField("Teacher Forgotten Password", default=False)
    otpVerified = models.BooleanField("OTP has been verified", default=False)
    otp = models.CharField("OTP Password", max_length=4, null=True)

    # Permissions
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='teacher_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='teacher_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    objects = TeacherManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = self.generate_unique_id()
        super(Teacher, self).save(*args, **kwargs)

    def generate_unique_id(self):
        while True:
            new_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            if not Teacher.objects.filter(id=new_id).exists():
                return new_id       

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
    displayImage = models.ImageField("Student Display Image", null=True, blank=True, upload_to=displayImageFilePath)

    # Parent Details
    parentName = models.TextField("Parents Name", max_length=30)
    parentEmail = models.EmailField("Parents Email Address", max_length=50)
    parentPhone = models.TextField("Parents Phone no.", max_length=13)

    # Teacher Linked
    # teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstName
