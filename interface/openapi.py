import requests

def _url(path):
    return 'https://api.open.ru' + path


def getcardlist():
    return requests.get(_url('/MyCards/1.0.0/MyCardsInfo/cardlist'))
