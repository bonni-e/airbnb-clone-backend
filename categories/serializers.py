from rest_framework import serializers
from .models import Category

'''
리팩토링 후 
'''

class CategorySerializer(serializers.ModelSerializer) :
    # 설정 
    # ㄴ 설정만 하면, 알아서 필드값들을 맵핑하고 -> create() update() 메소드까지 정의해줌
    class Meta : 
        model = Category
        
        # 보여줄 필드를 정해주거나 
        fields = (
            "name",
            "kind",
        )

        # 숨길 필드를 정해주면 됨 
        # exclude = (
        #     "kind",
        # )

'''
리팩토링 전 
class CategorySerializer(serializers.Serializer) :
    # Category가 가지고 있는 필드에 대한 설명을 해야함 
    # JSON 객체로 표현할 때, 어떤 자료형을 사용할지 Model과 일치하게 작성 
    # 보여주고 싶은 컬럼을 선택적으로 명시할 수 있음 

    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        required=True, 
        max_length=50
        )
    kind = serializers.CharField(
        max_length=15
    )
    # kind = serializers.ChoiceField(
    #     choices=Category.CategoryKindChoices.choices,
    # )
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data) :
        return Category.objects.create(**validated_data) 
        # **딕셔너리를 가져와서 자동으로 변환함 
        # {'name': '풀하우스', 'kind': 'full house'} ->
        # name = '풀하우스'
        # kind = 'full house'

        # create() 메소드는 객체를 반환해야 함 


    def update(self, instance, validated_data):
        # if validated_data['name'] : 
        #     instance.name = validated_data['name']

        instance.name = validated_data.get('name', instance.name)
        instance.kind = validated_data.get('kind', instance.kind)
        instance.save()
        return instance
'''
    
    