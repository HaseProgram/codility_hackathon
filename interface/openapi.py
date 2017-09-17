import requests

class BadResponseError(Exception):
	pass

class OpenAPI(object):

	def _url(path):
        return 'https://api.open.ru' + path

    def getcardlist():
        response = requests.get(self._url('/MyCards/1.0.0/MyCardsInfo/cardlist'))
        if response.status_code == 200:
            return response.json()['results']
        else:
        	raise BadResponseError



