from examples.models.example_model import ExampleModel


def create_example_model(uuid, text, char, binary, boolean):
    return ExampleModel(uuid, text, char, binary, boolean)


def get_example_model(uuid):
    return ExampleModel.objects.get(uuid=uuid)
