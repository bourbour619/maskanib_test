from django.conf import settings
import requests
from typing import Optional
from datetime import datetime
import logging

base_url = settings.TSETMC_API_URL

logger = logging.getLogger(__name__)

def get_indexes() -> Optional[...]:
    url = '{0}{1}'.format(base_url, 'Index/GetIndexB1LastAll/All/1/')
    print(url)
    try:
        headers = {'User-Agent': 'PostmanRuntime/7.32.3'}
        resp = requests.get(url, headers=headers)
        print(resp.json())
        indexes = resp.json()['indexB1']
        return ({'ins_code': i['insCode'], 'lval30': i['lVal30']} for i in indexes)
    except requests.exceptions.RequestException as exc:
        logger.error(exc)
        return None

def get_index_histories(ins_code: str) -> Optional[...]:
    url = '{0}{1}'.format(base_url, f'Index/GetIndexB2History/{ins_code}')
    try:
        resp = requests.get(url)
        histories = resp.json()['indexB2']
        return ({'date': datetime(year=h['dEven'][0:4],month=h['dEven'][4:6], day=h['dEven'][6:8]).strftime('%Y-%m-%d'), \
                'low':h['xNivInuPbMresIbs'], 'high': d['xNivInuPhMresIbs'], 'close': d['xNivInuClMresIbs']} for h in histories)
    except requests.exceptions.RequestException:
        return None