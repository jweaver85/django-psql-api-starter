from django.core import serializers as dserializers
from django.http import HttpResponse, JsonResponse
from rest_framework import serializers, fields
from rest_framework.views import APIView

from examples.serializers.example_model_serializer import ExampleModelSerializer
from examples.services.example_service import get_example_model, create_example_model


class GetSerializer(serializers.Serializer):
    uuid = fields.UUIDField()


class ExampleView(APIView):

    def get(self, request):
        serializer = GetSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)
        uuid = serializer.validated_data.get('uuid')

        resp_obj = get_example_model(uuid)
        serialized = ExampleModelSerializer(resp_obj)
        return JsonResponse(serialized.data)

    def create(self, request):
        uuid = request.GET.get('uuid')
        text = request.GET.get('text')
        char = request.GET.get('char')
        binary = request.GET.get('binary')
        boolean = request.GET.get('boolean')
        return create_example_model(
            uuid=uuid,
            text=text,
            char=char,
            binary=binary,
            boolean=boolean
        )

    def post(self, request):
        page = request.GET.get('page')
        limit = request.GET.get('page')
        return None

