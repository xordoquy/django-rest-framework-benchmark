import pytest
from django.utils import timezone
from django.contrib.auth import models
from drf_bench.core import serializers


def run_serializer(Serializer, data, many=True):
    serializer = Serializer(data, many=many)
    return serializer.data


def run_deserializer(Serializer, data, many=True):
    serializer = Serializer(data=data, many=many)
    validity = serializer.is_valid()
    print(serializer.errors)
    return validity


def generate_data(sample_size, base=False):
    if base:
        now = '2013-01-29T12:01'
    else:
        now = timezone.now()
    data = [{
                "id": i,
                "password": 'zmrjegar',
                "is_superuser": False,
                "username": 'user%i' % i,
                "first_name": 'john',
                "last_name": 'doe',
                "email": 'john.doe%i@local.host' % i,
                "is_staff": False,
                "is_active": False,
                "date_joined": now,
            } for i in range(sample_size)]
    return data


def generate_sample_data(sample_size=1, field_qt=1, default_data='test'):
    return [
        dict((('field%06i' % j, default_data) for j in range(field_qt)))
        for i in range(sample_size)
    ]


@pytest.mark.parametrize("sample_size", [1, 10, 100, 1000, 10000])
def test_model_serializer(benchmark, sample_size):
    data = [models.User(**kwargs) for kwargs in generate_data(sample_size)]
    result = benchmark(run_serializer, serializers.UserModel, data)
    assert result is not None


@pytest.mark.parametrize("sample_size", [1, 10, 100, 1000, 10000])
def test_serializer(benchmark, sample_size):
    data = generate_data(sample_size)
    result = benchmark(run_serializer, serializers.User, data)
    assert result is not None


@pytest.mark.parametrize("sample_size", [1, 10, 100, 1000, 10000])
def test_model_deserializer(benchmark, sample_size):
    data = generate_data(sample_size, base=True)
    result = benchmark(run_deserializer, serializers.UserModel, data)
    assert result is True


@pytest.mark.parametrize("sample_size", [1, 10, 100, 1000, 10000])
def test_deserializer(benchmark, sample_size):
    data = generate_data(sample_size, base=True)
    result = benchmark(run_deserializer, serializers.User, data)
    assert result is True


@pytest.mark.parametrize("field_qt", [1, 10, 100, 1000])
def test_model_serializer_field_qt(benchmark, field_qt, sample_size=1):
    data = generate_sample_data(
        sample_size=sample_size,
        field_qt=field_qt)
    result = benchmark(
        run_serializer,
        getattr(serializers, 'ModelCharField%06i' % field_qt),
        data)
    assert result is not None
