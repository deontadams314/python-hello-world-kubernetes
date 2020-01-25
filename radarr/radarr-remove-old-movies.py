import json, requests, sys

#radaar_url = "http://localhost:7878/api/movie/?apikey={}".format(api_key)
#http://localhost:8181/api/v2?apikey=a49af01b328547a1a6acf5abb1d72be0&cmd=get_library_media_info

global server_ip_address
server_ip_address = "192.168.1.60"

def radaar():
	global server_ip_address

	radaar_api_key = '68413a1b01dd41f8ba4532c27bad0b7b'
	radaar_url = 'http://{0}:7878/api/movie/?apikey={1}'.format(server_ip_address,radaar_api_key)
	#radaar_url = 'http://localhost:7878/api/movie/?apikey={0}'.format(radaar_api_key)
	radaar_response = requests.get(radaar_url)
	radaar_get = json.loads(radaar_response.text)

	radaar_movie_list = []
	radaar_movie_id = []

	for movie in radaar_get:
		if movie['sizeOnDisk'] != 0:
			radaar_movie_list.append(movie['title'])
			radaar_movie_id.append(movie['id'])

	return len(radaar_movie_list)

def tautulli():
	global server_ip_address
	tautulli_movie = []
	tautulli_year = []

	tautulli_api_key = 'a49af01b328547a1a6acf5abb1d72be0'
	#tautulli_url = 'http://localhost:8181/api/v2?apikey={0}&cmd=get_library_media_info&section_id=1&order_dir=asc&refresh=true&length={1}'.format(tautulli_api_key, radaar())
	tautulli_url = 'http://{0}:8181/api/v2?apikey={1}&cmd=get_library_media_info&section_id=1&order_dir=asc&refresh=true&length={2}'.format(server_ip_address,tautulli_api_key, radaar())
	tautulli_response = requests.get(tautulli_url)
	tautulli_get = json.loads(tautulli_response.text)

	print(tautulli_get)
	print(type(tautulli_get))


tautulli()


