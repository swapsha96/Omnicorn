import requests

API_URL = "http://narwhal.astro.yale.edu:8080"


def singleobject(id):
	params = {}
	if params['id'] is not None:
		params['id'] = id
	r = requests.get(API_URL + "/singleobject", params = params)
	result = r.json()
	return result

def conesearch(ra, dec, radius, unit = 'd'):
	params = {}
	if params['ra'] is not None:
		params['ra'] = ra
	if params['dec'] is not None:
		params['dec'] = dec
	if params['radius'] is not None:
		params['radius'] = radius
	params['unit'] = unit
	r = requests.get(API_URL + "/conesearch", params = params)
	result = r.json()
	return result

def nearest(ra, dec, unit = 'd'):
	params = {}
	if params['ra'] is not None:
		params['ra'] = ra
	if params['dec'] is not None:
		params['dec'] = dec
	params['unit'] = unit
	r = requests.get(API_URL + "/nearest", params = params)
	result = r.json()
	return result

def pointing(ra, dec, unit = 'd'):
	params = {}
	if params['ra'] is not None:
		params['ra'] = ra
	if params['dec'] is not None:
		params['dec'] = dec
	params['unit'] = unit
	r = requests.get(API_URL + "/pointing", params = params)
	result = r.json()
	return result

def pointing_id(id):
	params = {}
	if params['id'] is not None:
		params['id'] = id
	r = requests.get(API_URL + "/pointing_id", params = params)
	result = r.json()
	return result
