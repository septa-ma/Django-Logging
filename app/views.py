
from rest_framework.response import Response
from rest_framework.views import APIView
import logging
logger = logging.getLogger(__name__)

class Example_Log(APIView):

    def get(self, request):
        logger.error("this is error method of logger")
        logger.debug("this is debug method of logger")
        logger.info("this is info method of logger")
        logger.warning("this is warning method of logger")
        return Response("GET method for the API")

    def post(self, request):
        logger.error("this is error method of logger")
        logger.debug("this is debug method of logger")
        logger.info("this is info method of logger")
        return Response("POST method from the api")