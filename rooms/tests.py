# from django.test import TestCase
from rest_framework.test import APITestCase
from users.models import User
from categories.models import Category
from .models import * 

class TestRooms(APITestCase) :
    URL = "/api/v1/rooms/"
    
    def setUp(self) -> None:
        user = User.objects.create(username="admin")
        user.set_password("123")
        user.save()
        self.user = user

        Category.objects.create(name="원룸", kind="rooms")
        Amenity.objects.create(name="배스밤", description="bath bomb")
        Amenity.objects.create(name="냉장고", description="refregerator")

    def test_create_room(self) :
        # login 
        # self.client.login(username="admin", password="123")
        self.client.force_login(self.user)
        
        response = self.client.post(self.URL, data={
            "name" : "서초 오피스텔",
            "description" : "좋은 방",
            "rooms" : 1,
            "toilets" : 1,
            "address" : "서울시 서초구 방배동",
            "kind" : "private_room",
            "category" : 1,
            "amenities" : [1,2],
            "price" : 30000
        })
        print(response.json())

        self.assertNotEqual(response.status_code, 403, 'permission is denied')
        print(response.json())
        self.assertEqual(response.status_code, 200, 'status code is not 200')

class TestAmenities(APITestCase) :
    URL = "/api/v1/rooms/amenities/"
    NAME = "Amenity Test"
    DESC = "Amenity Description"

    # 테스트 실행 전 동작할 메소드 (Database)
    def setUp(self) -> None:
        user = User.objects.create(username="admin")
        user.set_password("123")
        user.save()
        self.user = user

        self.client.force_login(self.user)

        Amenity.objects.create(name=self.NAME, description=self.DESC)
        Amenity.objects.create(name=self.NAME, description=self.DESC)
        Amenity.objects.create(name=self.NAME, description=self.DESC)

    def test_all_amenities(self) :
        response = self.client.get(self.URL)

        # 테스트 케이스는 실제 데이터베이스에서 동작하지 않음 
        data = response.json()
        print(data)
        self.assertIsInstance(data, list)
        self.assertListEqual([len(data), data[0]["name"], data[0]["description"]], [3, self.NAME, self.DESC])

        self.assertEqual(response.status_code, 200, "Status code isn't 200")
    
    def test_create_amenity(self) :
        response = self.client.post(self.URL, data={"name":self.NAME, "description":self.DESC})
        data = response.json()
        print("data : ", data)

        self.assertIn("name", data)
        self.assertLessEqual(len(data["name"]), 180, 'name length over 180')
        self.assertListEqual([data["name"], data["description"]], [self.NAME, self.DESC])
        self.assertEqual(response.status_code, 200, "Not 200 status code.")


    # Sample
    # def test_two_plus_two(self) :
    #     # self.assertEqual(2+2, 4, "The math is wrong.")
    #     self.assertListEqual([2+2], [4], "The math is wrong.")

class TestAmenity(APITestCase) :
    URL = "/api/v1/rooms/amenities/"
    NAME = "Amenity Test"
    DESC = "Amenity Description"

    def setUp(self) -> None:
        user = User.objects.create(username="admin")
        user.set_password("123")
        user.save()
        self.user = user

        self.client.force_login(self.user)

        Amenity.objects.create(name=self.NAME, description=self.DESC)

    def test_amenity_not_found(self) :
        response = self.client.get(self.URL + '1')
        self.assertEqual(response.status_code, 200, 'Amenity not found')

    def test_get_amenity(self) :
        self.test_amenity_not_found()

        response = self.client.get(self.URL + '1')

        data = response.json()
        self.assertListEqual([data["name"], data["description"]], [self.NAME, self.DESC])
        self.assertEqual(response.status_code, 200)

    def test_update_amenity(self) :
        self.test_amenity_not_found()

        response = self.client.put(self.URL + '1', data={"name" : self.NAME, "discription" : self.DESC})
        data = response.json()

        self.assertIn("name", data)
        self.assertLessEqual(len(data["name"]), 180, 'name length over 180')
        self.assertListEqual([data["name"], data["description"]], [self.NAME, self.DESC])
        self.assertEqual(response.status_code, 200, "Not 200 status code.")

    def test_delete_amenity(self) :
        self.test_amenity_not_found()

        response = self.client.delete(self.URL + '1')
        
        self.assertEqual(response.status_code, 200)
    