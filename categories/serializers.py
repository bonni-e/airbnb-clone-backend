from rest_framework import serializers

class CategorySerializer(serializers.Serializer) :
    # Category가 가지고 있는 필드에 대한 설명을 해야함 
    # JSON 객체로 표현할 때, 어떤 자료형을 사용할지 Model과 일치하게 작성 
    # 보여주고 싶은 컬럼을 선택적으로 명시할 수 있음 

    pk = serializers.IntegerField()
    name = serializers.CharField(required=True)
    kind = serializers.CharField()
    # created_at = serializers.DateTimeField()