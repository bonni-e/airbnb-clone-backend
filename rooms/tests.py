# from django.test import TestCase
from rest_framework.test import APITestCase
from .models import * 

class TestAmenities(APITestCase) :
    URL = "/api/v1/rooms/amenities/"
    NAME = "Amenity Test"
    DESC = "Amenity Description"

    # 테스트 실행 전 동작할 메소드 (Database)
    def setUp(self) -> None:
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

        self.assertEqual(response.status_code, 200, "Not 200 status code.")
        self.assertListEqual([data["name"], data["description"]], [self.NAME, self.DESC])


    # Sample
    # def test_two_plus_two(self) :
    #     # self.assertEqual(2+2, 4, "The math is wrong.")
    #     self.assertListEqual([2+2], [4], "The math is wrong.")

    