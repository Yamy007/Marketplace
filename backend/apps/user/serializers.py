from .models import  ProfileModel
from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from django.db.transaction import atomic


UserModel = get_user_model()

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = "__all__"

class UserSerializer(ModelSerializer):
    profile = ProfileSerializer()
    class  Meta:
        model = UserModel
        fields = '__all__'
        extra_kwargs = {
            'password':{
                "write_only": True
            }
        }

    @atomic
    def create(self, validated_data):
        profile = validated_data.pop('profile')
        profile = ProfileModel.objects.create(**profile)
        user = UserModel.objects.create_user(profile=profile, **validated_data)
        return user
    
    
    @atomic
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        if not profile:
            instance.objects.update(**validated_data)
            instance.save()
        else:
            profile = ProfileModel.objects.get(id = instance.profile_id)
            profile.objects.update(**profile_data)
            profile.save()

        return instance