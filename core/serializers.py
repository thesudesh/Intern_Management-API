from rest_framework import serializers
from .models import UserProfile, Task, Attendance
from django.contrib.auth import authenticate

from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    """
    This serializer defines two fields for authentication:
      * username
      * password.
    It will try to authenticate the user with when validated.
    """
    email = serializers.EmailField(
        label="Email",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        # Take username and password from request
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)
            if not user:
                # If we don't have a regular user, raise a ValidationError
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        # We have a valid user, put it in the serializer's validated_data.
        # It will be used in the view.
        attrs['user'] = user
        return attrs


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'role', 'email', 'first_name', 'last_name', 'password']
    
    def create(self, validated_data):
        user = super().create(validated_data)
        password = validated_data.get("password")
        user.set_password("password")
        user.save()
        import ipdb; ipdb.set_trace()
        return user

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'assigned_to', 'completed']

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'user', 'check_in_time', 'check_out_time']

