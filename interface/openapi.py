import requests

class BadResponseError(Exception):
    pass

class BadRequest(Exception):
    def __init__(self, message):
        self.message  = message

class OpenAPI(object):

    def _url(self, path):
        return 'https://api.open.ru' + path

    def get_cardlist(self):
        response = requests.get(self._url('/MyCards/1.0.0/MyCardsInfo/cardlist'))
        if response.status_code == 200:
            return response.json()['Cards']
        else:
            raise BadResponseError

    def get_balance(self, cardId):
        header = { 'Accept': 'application/json' }
        data = { 'CardId' : cardId }
        response = requests.post(self._url('/MyCards/1.0.0/MyCardsInfo/balance'), headers = header, json = data)
        if response.status_code == 200:
            print(response)
            resp = response.json()
            print(resp)
            if resp['ErrorCode'] == '0':
                return resp['CardBalance'][0]
            else:
                raise BadRequest('Error occoured in balance query!')
        else:
            raise BadResponseError

    def get_transactions(self, cardId):
        header = { 'Accept': 'application/json' }
        data = { 'CardId' : cardId }
        response = requests.post(self._url('/MyCards/1.0.0/MyCardsInfo/history'), headers = header, json = data)
        if response.status_code == 200:
            resp = response.json()
            if resp['ErrorCode'] == '0':
                return resp['CardTransactionsList'][0]['CardTransaction']
            else:
                raise BadRequest('Error occured in transaction query!')
        else:
            raise BadResponseError
