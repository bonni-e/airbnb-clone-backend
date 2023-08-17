from rest_framework.serializers import ModelSerializer, ValidationError
from django.utils import timezone
from django.db import models
from .models import Booking

class RoomBookingSerializer(ModelSerializer) :
    # 필수값으로 변경 
    check_in = models.DateField()
    check_out = models.DateField()

    class Meta : 
        model = Booking
        fields = [
            "pk",
            "check_in",
            "check_out",
            "guests"
        ]

    # is_valid() 커스터마이징 
    # ㄴ validate_컬럼명 으로 만들기 
    def validate_check_in(self, value) :
        # 오류 반환 
        now = timezone.now().date()
        if now >= value : 
            raise ValidationError("유효하지 않은 기간입니다.")
        
        # 정상 반환 
        return value
    
    def validate_check_out(self, value) :
        now = timezone.now().date()
        if now >= value : 
            raise ValidationError("유효하지 않은 기간입니다.")
        return value
    
    def validate(self, attrs):
        room = attrs.get("room")
        print("room : ", room)

        check_in = attrs.get("check_in")
        check_out = attrs.get("check_out")

        if check_in >= check_out :
            raise ValidationError("유효하지 않은 기간입니다.")
        
        return super().validate(attrs)

class ExperienceBookingSerializer(ModelSerializer) :
    class Meta : 
        model = Booking
        fields = [
            "pk",
            "experience_time",
             "guests"
        ]

class BookingSerializer(ModelSerializer) :
    class Meta : 
        model = Booking
        fields = "__all__"