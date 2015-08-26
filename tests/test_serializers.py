import pytest
from django.utils import timezone
from django.contrib.auth import models
from drf_bench.core import serializers


def run_serializer(data, many=True):
    serializer = serializers.User(data, many=many)
    return serializer.data


def run_deserializer(data, many=True):
    serializer = serializers.User(data=data, many=many)
    validity = serializer.is_valid()
    print(serializer.errors)
    return validity


def run_model_serializer(data, many=True):
    serializer = serializers.UserModel(data, many=many)
    return serializer.data


def run_model_deserializer(data, many=True):
    serializer = serializers.UserModel(data=data, many=many)
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


def benchmark_serializer(benchmark, sample_size=1):
    data = generate_data(sample_size)
    result = benchmark(run_serializer, data)
    assert result is not None


def benchmark_model_serializer(benchmark, sample_size=1):
    data = [models.User(**kwargs) for kwargs in generate_data(sample_size)]
    result = benchmark(run_model_serializer, data)
    assert result is not None


def benchmark_deserializer(benchmark, sample_size=1):
    data = generate_data(sample_size, base=True)
    result = benchmark(run_deserializer, data)
    assert result is True


def benchmark_model_deserializer(benchmark, sample_size=1):
    data = generate_data(sample_size, base=True)
    result = benchmark(run_model_deserializer, data)
    assert result is True


@pytest.mark.parametrize("sample_size", [1, 10, 100, 1000, 10000])
def test_model_serializer(benchmark, sample_size):
    benchmark_model_serializer(benchmark, sample_size=sample_size)


@pytest.mark.parametrize("sample_size", [1, 10, 100, 1000, 10000])
def test_serializer(benchmark, sample_size):
    benchmark_serializer(benchmark, sample_size=sample_size)


@pytest.mark.parametrize("sample_size", [1, 10, 100, 1000, 10000])
def test_model_deserializer(benchmark, sample_size):
    benchmark_model_deserializer(benchmark, sample_size=sample_size)


@pytest.mark.parametrize("sample_size", [1, 10, 100, 1000, 10000])
def test_deserializer(benchmark, sample_size):
    benchmark_deserializer(benchmark, sample_size=sample_size)
