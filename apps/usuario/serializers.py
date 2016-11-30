from rest_framework.serializers import ModelSerializer

from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):

	class Meta:
		model = User
		fields = ('first_name', 'email')
