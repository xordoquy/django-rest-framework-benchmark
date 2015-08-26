drf_bench
=========

A few benchs to understand how playing on various degrees play on the
Django REST framework performance:

- size of the data to (de)serialize
- ModelSerializer vs Serializer
- Serialize vs Deserialize
- number of fields to process


How to run them
---------------

Prior to the run, create / activate a virtualenv.

    git clone https://github.com/xordoquy/django-rest-framework-benchmark.git
    cd django-rest-framework-benchmark
    pip install -e .[tests]
    py.test
