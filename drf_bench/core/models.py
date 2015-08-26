from django.db import models


def generate_model(
        field_name='CharField',
        field_quantity=1,
        field_type=models.CharField,
        field_arguments=None):

    class_name = 'Model%s%06i' % (field_name, field_quantity)

    class Meta:
        db_table = 'model_%s_%06i' % (field_type, field_quantity)

    if not field_arguments:
        field_arguments = {}

    attrs = dict((
        ('field%06i' % i, field_type(**field_arguments))
        for i in range(field_quantity)))

    attrs.update({'__module__': 'drf_bench.core', 'Meta': Meta})

    model = type(class_name, (models.Model,), attrs)
    return model


charfield_kwargs = {
    'max_length': 256,
}

ModelCharField000001 = generate_model('CharField',    1, models.CharField, charfield_kwargs)
ModelCharField000010 = generate_model('CharField',   10, models.CharField, charfield_kwargs)
ModelCharField000100 = generate_model('CharField',  100, models.CharField, charfield_kwargs)
ModelCharField001000 = generate_model('CharField', 1000, models.CharField, charfield_kwargs)
