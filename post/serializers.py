from rest_framework import serializers
from .models import Post, Category


class PostListSerializer(serializers.ModelSerializer):
    class Meta():
        model = Post
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

"""     def to_representation(self, instance):
        return {
            'id': instance.id,
            'title': instance.title,
            'description': instance.description,
            'created': instance.created,
            'user': instance.user.id,
            'category': instance.category.id,
            'category_name': instance.category.name,
        } """

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta():
        model = Category
        fields = '__all__'