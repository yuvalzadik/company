import requests


def get_workers():
    workers = requests.get(url="http://localhost:80/workers")
    if workers.status_code != 200:
        return False
    return True


print(get_workers())