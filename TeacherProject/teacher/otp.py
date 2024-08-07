from random import randint
from django.core.mail import send_mail

def createOTP():
    return str(randint(1000, 9999))

def sendOTP(email: str, otp: str):
    try:
        send_mail(
            subject="Teacher App OTP",
            message=f"Your OTP to reset your password is {otp}. Please do not share this OTP with anyone.",
            recipient_list=[email],
            from_email="teacherappinternship@gmail.com"
        )
        return True # Success
    except Exception as e:
        print(e)
        return False # Failed