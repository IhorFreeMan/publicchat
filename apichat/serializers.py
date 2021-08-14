# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import ChatModel


class ChatSerializer(serializers.ModelSerializer):
    """Chat Serializer"""
    class Meta:
        model = ChatModel
        fields = ['id', 'email', 'body', 'created', 'updated']



class ChatAddSerializer(serializers.ModelSerializer):
    """Add Chat"""

    def validate(self, data):
        if len(str(data['body'])) > 100:
            print(len(data['body']))
            raise serializers.ValidationError("Text must be less than 100 characters")
        return data

    class Meta:
        model = ChatModel
        fields = ['email', 'body', 'created', 'updated']