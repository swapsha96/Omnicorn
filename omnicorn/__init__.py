import requests

API_URL = "http://narwhal.astro.yale.edu:8080"


def singleobject(id):
	params = {}
	if id is not None:
		params['id'] = id
	r = requests.get(API_URL + "/singleobject", params = params)
	if r.status_code == 200:
		result = r.json()
	else:
		result = r.content
	return result

def conesearch(ra, dec, radius, unit = 'd'):
	params = {}
	if ra is not None:
		params['ra'] = ra
	if dec is not None:
		params['dec'] = dec
	if radius is not None:
		params['radius'] = radius
	params['unit'] = unit
	r = requests.get(API_URL + "/conesearch", params = params)
	if r.status_code == 200:
		result = r.json()
	else:
		result = r.content
	return result

def nearest(ra, dec, unit = 'd'):
	params = {}
	if ra is not None:
		params['ra'] = ra
	if dec is not None:
		params['dec'] = dec
	unit = unit
	r = requests.get(API_URL + "/nearest", params = params)
	if r.status_code == 200:
		result = r.json()
	else:
		result = r.content
	return result

def pointing(ra, dec, unit = 'd'):
	params = {}
	if ra is not None:
		params['ra'] = ra
	if dec is not None:
		params['dec'] = dec
	params['unit'] = unit
	r = requests.get(API_URL + "/pointing", params = params)
	if r.status_code == 200:
		result = r.json()
	else:
		result = r.content
	return result

def pointing_id(id):
	params = {}
	if id is not None:
		params['id'] = id
	r = requests.get(API_URL + "/pointing_id", params = params)
	if r.status_code == 200:
		result = r.json()
	else:
		result = r.content
	return result
