from django.db import models

# Create your models here.
class CommonModel(models.Model) :

    """ Common Model Definition """
    
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    # CommonModel 에 대한 테이블 생성을 막고, (Database)
    # 다른 애플리케이션에서 재사용할 수 있는 형태임을 알림 
    class Meta:
        abstract = True
