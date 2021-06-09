from rest_framework import serializers
from .models import Child


class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = '__all__'

    def create(self, validated_data):
        child = Child.objects.create(
            passport_image=validated_data['passport_image'],
            first_name=validated_data['first_name'],
            middle_name=validated_data['middle_name'],
            surname=validated_data['surname'],
            age=validated_data['age'],
            gender=validated_data['gender'],
            talent=validated_data['talent'],
            medical_records=validated_data['medical_records'],
            school_report=validated_data['school_report'],
        )

        child.save()
        return child

    def update(self, instance, validated_data):
        instance.passport_image = validated_data.get('passport_image', instance.passport_image)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.middle_name = validated_data.get('middle_name', instance.middle_name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.age = validated_data.get('age', instance.age)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.talent = validated_data.get('talent', instance.talent)
        instance.medical_records = validated_data.get('medical_records', instance.medical_records)
        instance.school_report = validated_data.get('school_report', instance.school_report)

        instance.save()
        return instance
