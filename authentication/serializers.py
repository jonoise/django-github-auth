from django.contrib.auth import get_user_model
from rest_framework import serializers
# from .models import Profile


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'password']
        extra_kwargs = {"password": {'write_only': True, "min_length": 8}}

    def create(self, validated_data):
        # Fue necesario usar el "create_user" method para que el password fuera
        # hasheado correctamente.
        return get_user_model().objects.create_user(**validated_data)


# class ProfileSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Profile
#         fields = ['user', 'first_name', 'last_name', 'email', 'image']
