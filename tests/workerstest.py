import requests


def test_get_workers():
    workers = requests.get(url="http://localhost:8082/workers")
    if workers.status_code != 200:
        return False
    return True

def test_add_workers():
    workers = requests.get(url="http://localhost:8082/workers")
    if workers.status_code != 200:
        return False
    return True






print(test_get_workers())