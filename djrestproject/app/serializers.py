from rest_framework import serializers
from .models import UserModel,Student

class UserSerializer(serializers.HyperlinkedModelSerializer):
    # add this
    # url = serializers.HyperlinkedIdentityField(UserViewset="app:UserViewset")
    class Meta:
        model=UserModel
        fields=['id','name','age','email','contact_no']
class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Student
        fields=['id','url','sname','roll_no','place']
