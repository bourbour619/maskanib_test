import json
from celery import shared_task
from celery.utils.log import get_task_logger
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from api.serializers import TseTmcIndexSerializer, TseTmcIndexHistorySerializer
from api.models import Index
from api.helper import get_indexes, get_index_histories

logger = get_task_logger(__name__)


@shared_task
def tsetmc_indexes_with_histories(update: bool = False) -> None:
    task_name = tsetmc_indexes_with_histories.__name__
    logger.info('[%s] task started ...' % task_name)
    try:
        for index in get_indexes():
            serializer = TseTmcIndexSerializer(data=index)
            if serializer.is_valid():
                serializer.save()
                logger.info('index %s saved' %
                            serializer.validated_data['ins_code'])
            else:
                logger.error(serializer.errors)
                logger.error('index %s failed' % serializer.data['insCode'])

        for index in Index.objects.all():
            histories = get_index_histories(index.ins_code)
            histories = (list(histories)[-1], ) if update else histories
            for history in histories:
                serializer = TseTmcIndexHistorySerializer(data=history)
                if serializer.is_valid():
                    serializer.save()
                    logger.info('index history for index %(index)s and date %(date)s saved' %
                                {'index': serializer.validated_data['index_id'], 'date': serializer.validated_data['date']})
                else:
                    logger.error(serializer.errors)
                    logger.error('index history for index %(index)s and date %(date)d failed' %
                                 {'index': serializer.data['insCode'], 'date': serializer.data['dEven']})
    except Exception as ex:
        logger.info('[%s] task stopped ...' %
                    task_name)
        logger.error(ex)
    else:
        if not update:
            schedule, created = IntervalSchedule.objects.get_or_create(
                every=60,
                period=IntervalSchedule.SECONDS,
            )

            periodic_task = PeriodicTask.objects.create(
                interval=schedule,
                name=task_name,
                task='api.tasks.%s' % task_name,
                kwargs=json.dumps({
                    'update': True,
                }),
            )
            logger.info('[%s] periodic_task will run every %d seconds' %
                        periodic_task.name, periodic_task.interval.every)
        logger.info('[%s] task finished ...' % task_name)
