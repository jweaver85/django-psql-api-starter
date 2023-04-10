from rest_framework import serializers

from examples.models.example_model import ExampleModel


class ExampleModelSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    text = serializers.CharField()
    char = serializers.CharField()
    binary = serializers.CharField()
    boolean = serializers.BooleanField()

    # class Meta:
    #     model = ExampleModel
    #     fields = '__all__'

