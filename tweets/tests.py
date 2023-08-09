from rest_framework.test import APITestCase
from users.models import User
from .models import Tweet

class TestTweets(APITestCase) :
    URL = "/api/v1/tweets/"

    def setUp(self) -> None:
        user = User.objects.create(username="admin")
        user.set_password("123")
        user.save() 
        self.user = user

    def test_get_tweets(self) :
        response = self.client.get(self.URL)
        data = response.json()
        print("data : ", data)
        self.assertIsInstance(data, list, 'Response data is not List.')
        self.assertEqual(response.status_code, 200, 'Status code is not 200.')

    def test_post_tweet(self) :
        self.client.force_login(self.user)
        response = self.client.post(self.URL, data={
            "payload" : "hello world"
        })
        self.assertNotEqual(response.status_code, 403, 'Permission denied.')
        self.assertIsInstance(response.json().get("payload"), str,'Payload is required.')
        self.assertEqual(response.status_code, 200, 'Status code is not 200.')

class TestTweet(APITestCase) :
    URL = "/api/v1/tweets/1/"

    def setUp(self) -> None:
        user = User.objects.create(username="admin")
        user.set_password("123")
        user.save() 
        self.user = user
        
        Tweet.objects.create(payload="hello world")
    
    def test_tweet_not_found(self) :
        response = self.client.get(self.URL)
        self.assertEqual(response.status_code, 200, 'Tweet is not found.')

    def test_get_tweet(self) :
        self.test_tweet_not_found()

        response = self.client.get(self.URL)
        data = response.json()
        self.assertEqual(data["payload"], "hello world", 'Response data is wrong.')
        self.assertEqual(response.status_code, 200, 'Status code is not 200.')

    def test_put_tweet(self) :
        self.test_tweet_not_found()

        self.client.force_login(self.user)

        response = self.client.put(self.URL, data={
            "payload" : "Halo~"
        })
        data = response.json()

        self.assertNotEqual(response.status_code, 403, 'Permission denied.')
        self.assertEqual(data["payload"], "Halo~", "Response data is wrong.")
        self.assertEqual(response.status_code, 200, 'Status code is not 200.')

    def test_delete_tweet(self) :
        self.test_tweet_not_found()

        self.client.force_login(self.user) 

        response = self.client.delete(self.URL)
        
        self.assertNotEqual(response.status_code, 403, 'Permission denied.')
        self.assertEqual(response.status_code, 200, 'Status code is not 200.')