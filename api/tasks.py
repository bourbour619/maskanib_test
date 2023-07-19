from celery import shared_task
from celery.utils.log import get_task_logger
from api.serializers import IndexSerializer
from api.helper import get_indexes

logger = get_task_logger(__name__)

@shared_task
def create_or_update_indexes():
    indexes = get_indexes()
    for index in indexes:
        serializer = IndexSerializer(data=index)
        if serializer.is_valid():
            serializer.save()
            logger.info('index %s saved' %index['ins_code'])
        else:
            logger.error(serializer.errors)
            logger.error('index %s failed' %index['ins_code'])


@shared_task
def create_or_update_index_histories():
    pass