import sys

sys.path.insert(0, "src/vendor")

from aws_lambda_powertools import Logger

logger = Logger(
    log_record_order=["level", "message"],
)
logger.remove_keys(["service"])
