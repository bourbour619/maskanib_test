from django.conf import settings
import requests
from typing import Optional
from datetime import datetime
import logging

base_url = settings.TSETMC_API_URL
base_header = {
    'User-Agent': settings.TSETMC_REQUIRED_USER_AGENT
}

logger = logging.getLogger(__name__)


def get_indexes() -> Optional[...]:
    url = '{0}{1}'.format(base_url, 'Index/GetIndexB1LastAll/All/1/')
    try:
        resp = requests.get(url, headers=base_header)
        indexes = resp.json()['indexB1']
        return (index for index in indexes)
    except requests.exceptions.RequestException as ex:
        logger.error(ex)
        return None


def get_index_histories(ins_code: str) -> Optional[...]:
    url = '{0}{1}'.format(base_url, f'Index/GetIndexB2History/{ins_code}')
    try:
        resp = requests.get(url, headers=base_header)
        histories = resp.json()['indexB2']
        return (history for history in histories)
    except requests.exceptions.RequestException as ex:
        logger.error(ex)
        return None
