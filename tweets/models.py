from django.db import models
from common.models import CommonModel

# Create your models here.
class Tweet(CommonModel) :
    payload = models.CharField(max_length=180)
    user = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return "{name} : {msg}".format(name=self.user, msg=self.payload)

class Like(CommonModel) :
    user = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True)
    tweet = models.ForeignKey("tweets.Tweet", on_delete=models.CASCADE)

