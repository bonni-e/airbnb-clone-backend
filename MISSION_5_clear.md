# REST Framework

- 오늘의 강의: 에어비앤비 클론코딩: From #10.0 to #10.09
- 제출기간: 익일 오전 6시까지

---
## Mission:
- When the user goes to /api/v1/tweets, show a list of all the Tweets on your database.
- When the user goes to /api/v1/users/<user_id>/tweets show a list of all the Tweets created by a User
- 유저가  이동하면, 데이터베이스의 모든 Tweets 리스트를 보여줘야 한다./api/v1/tweets
- 유저가 /api/v1/users/<user_id>/tweets 이동하면, User 가 만든 모든 Tweets 리스트를 보여줘야 한다.

---
## Requirements:
- DON'T use the ModelSerializer class.
- DON'T use the APIView class.
- Use models.Serializer
- Handle User.DoesNotExists

---
## Notes:
- There is already an admin user. Username: admin Password: 123456
- Django Rest Framework is already installed.
- 이미 어드민 유저가 있습니다. (유저명: admin. 비밀번호: 123456) 입니다.
- Django Rest Framework 는 이미 설치되어 있습니다.
