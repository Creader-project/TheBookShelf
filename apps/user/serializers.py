# _*_ coding: utf-8 _*_

__author__ = 'Tim'
__date__ = '15/08/2021 21:47'

from rest_framework import serializers
from .models import AuthUser


class RegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for registering a new user.
    """
    class Meta:
        model = AuthUser
        fields = ('email', 'username', 'password', 'first_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UsersSerializer(serializers.ModelSerializer):
    """
    Serializer for users.
    """
    class Meta:
        model = AuthUser
        fields = "__all__"
