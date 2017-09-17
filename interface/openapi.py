import requests

class BadResponseError(Exception):
    pass

class BadRequest(Exception):
    def __init__(self, message)
        self.message  = message

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
        	r = response.json()
            if r['ErrorCode'] == 0:
            	return r['CardBalance'][0]
            else:
            	raise BadRequest(r['ErrorDescription'])
        else:
            raise BadResponseError

    def gettransactions(self, cardId):
        h = { 'Accept': 'application/json' }
        d = { 'CardId' : cardId }
        response = requests.post(self._url('/MyCards/1.0.0/MyCardsInfo/history'), headers = h, json = d)
        if response.status_code == 200:
        	r = response.json()
            if r['ErrorCode'] == 0:
                return r['CardTransactionsList'][0]['CardTransaction']
            else:
            	raise BadRequest('Error occured in transaction query!')
        else:
            raise BadResponseError
