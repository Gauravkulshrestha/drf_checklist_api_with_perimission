from rest_framework import serializers
from .models import Checklist, ChecklistItem
from django.contrib.auth.models import User

class ChecklistItemSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = ChecklistItem
        fields = ['id', 'text', 'is_checked', 'created_on', 'updated_on', 'checklist', 'user']

class ChecklistSerializer(serializers.ModelSerializer):
    checklist = ChecklistItemSerializer(many=True, read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Checklist
        fields = ['id', 'title', 'is_deleted', 'is_archived', 'created_on', 'updated_on', 'checklist', 'user']

class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
        extra_kwargs = {
            'password1': {'write_only': True},
            'password2': {'write_only': True}
        }

    def create(self, validated_data):
        email = validated_data['email']
        username = validated_data['username']
        password1 = validated_data['password1']
        password2 = validated_data['password2']            
        user = User(email=email, username=username)

        if password1 == password2:
            user.set_password(validated_data['password1'])
            user.save()
            return user
        else:
            raise serializers.ValidationError({
                'error':'Password does not match!'
            })