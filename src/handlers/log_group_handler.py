from src.application.services.log_group.tag_log_group_service import (
    TagLogGroupService,
)


def add_name_tag(event, context):
    return TagLogGroupService().add_name_tag()
