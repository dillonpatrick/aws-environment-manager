from src.application.services.iam import TagIamService


def add_name_tag(event, context):
    return TagIamService().add_name_tag()
