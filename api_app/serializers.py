from rest_framework import serializers
from api_app.models import User,Member,Activity



class ActivitySerializer(serializers.ModelSerializer):
	class Meta:
		model=Activity
		fields=['start_date','end_date']


class UserSerializer(serializers.ModelSerializer):
	activity_periods = ActivitySerializer(many=True,read_only=True)
	class Meta:
		"""docstring for Meta"""
		model = User
		fields =['ids','real_name','tz','activity_periods']

		

class MemberSerializer(serializers.ModelSerializer):
	members = UserSerializer(many=True,read_only=True)

	class Meta:
		"""docstring for Meta"""

		model = Member
		fields =['ok','members']
