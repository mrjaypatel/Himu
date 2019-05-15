def sendMe(qty, item):
	# importing the requests library
	import requests
	# api-endpoint
	URL = "http://himu.humbingo.com/sendMe.php"
	# defining a params dict for the parameters to be sent to the API
	PARAMS = {'qty':qty,'item': item}
	# sending get request and saving the response as response object
	r = requests.get(url = URL, params = PARAMS)
	data = r.json()
	msg = data['msg']
	print(msg)