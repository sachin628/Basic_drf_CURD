from django.db.models import fields
from rest_framework import serializers
from .models import Items

class ItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Items
		fields = ('category','name', 'amount')
