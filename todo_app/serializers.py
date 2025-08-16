from rest_framework import serializers
from todo_app.models import Task


class TaskSerializer(serializers.Serializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed', 'created_at']

    def create(self, validated_data):
        return Task(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.completed = validated_data.get('completed', instance.completed)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        return instance
