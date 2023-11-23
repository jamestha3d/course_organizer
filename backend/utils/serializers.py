from rest_framework import serializers


class FlexibleSerializer(serializers.ModelSerializer):
    """
    Serializer class for flexible field definitions, allowing
    dynamically adding/removing of fields without needing to make
    a new serializer.
    """
    def __init__(self, *args, **kwargs):
        remove_fields = kwargs.pop('remove_fields', None)
        super(FlexibleSerializer, self).__init__(*args, **kwargs)

        if remove_fields:
            for field_name in remove_fields:
                self.fields.pop(field_name)

    def apply_and_save(self, instance, data):
        for attr, value in data.items():
            setattr(instance, attr, value)
        instance.save()

    def get_field_names(self, declared_fields, info):
        expanded_fields = super(FlexibleSerializer, self).get_field_names(declared_fields, info)
        if getattr(self.Meta, 'extra_fields', None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields
