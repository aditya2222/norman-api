from rest_framework import serializers
from .models import PersonalData


class employeeSerializer(serializers.ModelSerializer):

	class Meta:
		model = PersonalData
		fields = '__all__'