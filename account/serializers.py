from rest_framework import serializers

from .models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields='first_name', 'last_name', 'password', 'username'

    def create(self, validated_data):
        user = CustomUser(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user