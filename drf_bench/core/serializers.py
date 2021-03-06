from django.core import validators
from django.contrib.auth import models as auth_models
from rest_framework import serializers
from . import models


class NullMixin(object):
    def create(self, validated_data):
        return None

    def udpate(self, instance, validated_data):
        return None


class UserModel(NullMixin, serializers.ModelSerializer):
    class Meta:
        model = auth_models.User
        fields = (
            'id', 'password', 'last_login', 'is_superuser', 'username',
            'first_name', 'last_name', 'email', 'is_staff', 'is_active',
            'date_joined',
        )
        extra_kwargs = {
            'username': {
                'validators': [
                    validators.RegexValidator(
                        r'^[\w.@+-]+$',
                        ('Enter a valid username. This value may contain only '
                         'letters, numbers ' 'and @/./+/-/_ characters.')
                    ),
                ],
            },
        }


class User(NullMixin, serializers.Serializer):
    id = serializers.IntegerField(
        label='ID', read_only=True)
    password = serializers.CharField(
        max_length=128)
    last_login = serializers.DateTimeField(
        allow_null=True, required=False)
    is_superuser = serializers.BooleanField(
        help_text='Designates that this user has all permissions without explicitly assigning them.',
        label='Superuser status', required=False)
    username = serializers.CharField(
        help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.',
        max_length=30,
        validators=[
            validators.RegexValidator(
                r'^[\w.@+-]+$',
                ('Enter a valid username. This value may contain only '
                  'letters, numbers ' 'and @/./+/-/_ characters.')
            ),
        ])
    first_name = serializers.CharField(
        allow_blank=True, max_length=30, required=False)
    last_name = serializers.CharField(
        allow_blank=True, max_length=30, required=False)
    email = serializers.EmailField(
        allow_blank=True, label='Email address',
        max_length=254, required=False)
    is_staff = serializers.BooleanField(
        help_text='Designates whether the user can log into this admin site.',
        label='Staff status', required=False)
    is_active = serializers.BooleanField(
        help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.',
        label='Active', required=False)
    date_joined = serializers.DateTimeField(
        required=False)


class ModelCharField000001(NullMixin, serializers.ModelSerializer):
    class Meta:
        model = models.ModelCharField000001


class ModelCharField000010(NullMixin, serializers.ModelSerializer):
    class Meta:
        model = models.ModelCharField000010


class ModelCharField000100(NullMixin, serializers.ModelSerializer):
    class Meta:
        model = models.ModelCharField000100


class ModelCharField001000(NullMixin, serializers.ModelSerializer):
    class Meta:
        model = models.ModelCharField001000
