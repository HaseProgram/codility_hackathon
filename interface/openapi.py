import requests

class BadResponseError(Exception):
    pass

class OpenAPI(object):

    def _url(self, path):
        return 'https://api.open.ru' + path

    def getcardlist(self):
        response = requests.get(self._url('/MyCards/1.0.0/MyCardsInfo/cardlist'))
        if response.status_code == 200:
            return response.json()['Cards']
        else:
            raise BadResponseError

    def getbalance(self, cardId):
        h = { 'Accept': 'application/json' }
        d = { 'CardId' : cardId }
        response = requests.post(self._url('/MyCards/1.0.0/MyCardsInfo/balance'), headers = h, json = d)
        if response.status_code == 200:
            return response.json()['CardBalance'][0]
        else:
            print(response.status_code)
            raise BadResponseError

    def gettransactions(self, cardId):
        h = { 'Accept': 'application/json' }
        d = { 'CardId' : cardId }
        response = requests.post(self._url('/MyCards/1.0.0/MyCardsInfo/history'), headers = h, json = d)
        if response.status_code == 200:
            return response.json()['CardTransactionsList'][0]['CardTransaction']
        else:
            print(response.status_code)
            raise BadResponseError
