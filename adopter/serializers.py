from rest_framework import serializers
from .models import Adopter


class AdopterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adopter
        fields = '__all__'

    def create(self, validated_data):
        adopter = Adopter.objects.create(
            passport_image=validated_data['passport_image'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            surname=validated_data['surname'],
            gender=validated_data['gender'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            id_number=validated_data['id_number'],
            location=validated_data['location'],
            marital_status=validated_data['marital_status'],
        )

        adopter.save()
        return adopter

    def update(self, instance, validated_data):
        instance.passport_image = validated_data.get("passport_image", instance.passport_image),
        instance.first_name = validated_data.get("first_name", instance.first_name),
        instance.last_name = validated_data.get("last_name", instance.last_name),
        instance.surname = validated_data.get("surname", instance.surname),
        instance.gender = validated_data.get("gender", instance.gender),
        instance.email = validated_data.get("email", instance.email),
        instance.phone_number = validated_data.get("phone_number", instance.phone_number),
        instance.id_number = validated_data.get("id_number", instance.id_number),
        instance.location = validated_data.get("location", instance.location),
        instance.marital_status = validated_data.get("marital_status", instance.marital_status),

        instance.save()
        return instance
