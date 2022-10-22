import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
  logger.info("Incoming event: {}".format(event))

  return {
    "statusCode": 200,
    "body": "A message from the docker lambda!"
  }