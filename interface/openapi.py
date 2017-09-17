import urllib.request as requests
#TODO 
def _url(path):
    return 'https://api.open.ru' + path


def getcardlist():
	try:
		response = requests.get(_url('/MyCards/1.0.0/MyCardsInfo/cardlist'))
	except:
		raise 
	return response
