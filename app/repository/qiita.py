from model.qiita import QiitaInfo
from repository.config import CONFIG
import requests

QIITA_URL = "https://qiita.com/"

def load_qiita_info(item_id: str) -> QiitaInfo:
    headers = {
        'Content-Type': 'application/json',
        'Charset': 'utf-8',
        'Authorization': 'Bearer {}'.format(CONFIG.qiita_access_token)
    }
    response = requests.get(QIITA_URL + "api/v2/items/" + item_id, headers=headers)
    if response.status_code == 200:
        data = response.json()
        qiita_info = QiitaInfo(data)
        return qiita_info
    else:
        raise Exception(f"Failed to load Qiita info. Status code: {response.status_code}")