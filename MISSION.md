# Models

- 오늘의 강의: 에어비앤비 클론코딩: From #6.0 to #6.11
- Today we are going to practice creating Apps, Models and Foreign Keys.
- 코딩 시작입니다! 오늘은 Apps, Models 그리고 Foreign Keys 를 연습합니다.
- 제출기간: 익일 오전 6시까지

---

## Mission
- Create and install an app named tweets.
- The tweets app should have the models: Tweet and Like.
- Build the admins for the Tweet and Like models.
- tweets 라는 이름의 앱을 생성하고 설치하세요.
- tweets앱은 Tweet 그리고 Like 라는 models 이 있어야 합니다.
- Tweet 그리고 Like models 을 위한 어드민을 만드세요.

--- 

## Tweet Model Fields
- payload: Text(max. lenght 180)
- user: ForeignKey
- created_at: Date
- updated_at: Date

---

## Like
- user: ForeignKey
- tweet: ForeignKey
- created_at: Date
- updated_at: Date

---

## Requirements:
- Use abstract classes.
- Customize the __str__ method of all classes.

---

## Notes:
- There is already an admin user. Username: admin Password: 123456
- 이미 어드민 유저가 있습니다. (유저명: admin. 비밀번호: 123456) 입니다.

--- 

## How to use Replit + Django?

---

## 제출방법
- 코딩 챌린지는 Repl.it 라는 툴을 이용하여 제출합니다. 사용방법
- 제출기간: 익일 오전 6시까지
- 야호! 토요일. 일요일은 휴일 입니다