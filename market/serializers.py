from rest_framework import serializers

from .models import Stock


class People:
    def __init__(self,name,age,gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender


class PeopleSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()
    gender = serializers.CharField()

    def validate_name(self,name):
        return name

    def validate(self, attrs):
        if attrs['age'] < 18:
            raise serializers.ValidationError('Возраст должен быть не менее 18')
        return super().validate(attrs)

    def create(self, validated_data):
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'
        

