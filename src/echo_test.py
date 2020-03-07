import json
import urllib2

def test_echo():
	response = urllib2.urlopen('http://127.0.0.1:8080/echo?data=echo')
	data = json.load(response)
	print(data)