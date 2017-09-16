import urllib.request as requests

def _url(path):
    return 'https://api.open.ru' + path


def getcardlist():
<<<<<<< HEAD
	try:
		response = requests.get(_url('/MyCards/1.0.0/MyCardsInfo/cardlist'))
	except:
		raise 
	return response
=======
    return requests.get(_url('/MyCards/1.0.0/MyCardsInfo/cardlist'), {"Accept": "application/json"})
>>>>>>> 92013437248323ad34c11e238cf8b98f01a02ce8
