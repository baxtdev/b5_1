from rest_framework import serializers

from .models import Product,Category


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    parent_category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), allow_null=True, required=False)
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'parent_category']

    def create(self, validated_data):
        return self.Meta.model.objects.create(**validated_data)

    def update(self, validated_data):
        instance = self.Meta.model.objects.get(pk=validated_data['id'])
        instance.name = validated_data.get('name', instance.name)
        instance.parent_category = validated_data.get('parent_category', instance.parent_category)
        instance.save()
        return instance




        

