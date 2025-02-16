from src.application.services.secrets_manager import (
    ReplicateSecretService,
    TagSecretService,
    UnusedSecretsServices,
)


def replicate_secret(event, context):
    return ReplicateSecretService().replicate_secrets()


def add_name_tag(event, context):
    return TagSecretService().add_name_tag()


def unused_secrets(event, context):
    return UnusedSecretsServices().delete_unused_secrets()
