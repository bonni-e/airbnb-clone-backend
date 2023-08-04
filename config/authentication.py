from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from users.models import User

# User 를 반환하는 나만의 인증-권한 클래스 
class UsernameAuthentication(BaseAuthentication) :

    # 필수로 오버라이드 해야하는 메소드
    # ㄴ reuqest는 user가 없는 객체임 (header를 보고 직접 user를 찾아줘야 함) 
    # ㄴ 유저를 찾지 못한 경우, 반드시 None 반환 
    def authenticate(self, request):
        print(request.headers)
        username = request.headers.get("X-USERNAME")

        # 예외1) 헤더 정보 없이 요청이 들어왔을 때 
        if not username :
            return None
        
        try :
            user = User.objects.get(username=username)
            # 규칙) user가 앞에 오는 다음과 같은 튜플을 반환해야만 함 
            return (user, None)
        except User.DoesNotExist :
            # 예외2) 헤더 정보는 있지만 찾는 유저가 없는 경우 
            raise exceptions.AuthenticationFailed(f'No user {username}')