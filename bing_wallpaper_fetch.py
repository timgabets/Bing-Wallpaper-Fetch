import urllib.request
import binascii
import json
import wget
import sys
import getopt
import os

def get_image_names(n):
	images = {}
	url = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n={}&mkt=en-US'.format(n)

	try:
		raw_data = urllib.request.urlopen(url).read().decode('utf-8')
		image_data = json.loads(raw_data)['images']
			
		for i in image_data:
			date = i['startdate']
			images[date] = i['url'].split('/')[-1].replace('1920x1080.jpg', '')
	except:
		raise

	return images

def fetch(n):
	"""
	Fetch n last images.
	Trying to get 1920x1200 images first, if not found 1920x1080 images are fetched then.
	Also note that the 1920x1200 images are watersigned with the Bing logo, while 1920x1080 images are not.
	"""
	servers = ['az619822', 'az608707']
	resolutions = ['1920x1200.jpg', '1920x1080.jpg']
	images = get_image_names(n)

	for date in images:
		for res in resolutions:
			try:
				url = 'http://{}.vo.msecnd.net/files/{}{}'.format(servers[0], images[date], res)
				print('\nFetching image {}: {}'.format(date, url))
				filename = wget.download(url)
				break
			except urllib.error.HTTPError as e:
				print(e.code, e.reason)

def show_help(name):
	print('Usage: python3 {} [OPTIONS]... '.format(name))
	print('Fetch Bing Wallpaper images (according to the Bing\'s API restrictions fetching only the last 16 images is allowed)')
	print('  -c, --count=[COUNT]\t\t\tThe number of images to fetch')
	print('  -d, --output-directory=[DIRECTORY]\tOutput directory to put the images to')

if __name__ == '__main__':	
	optlist, args = getopt.getopt(sys.argv[1:], 'hc:d:', ['help', 'count=', 'output-directory='])
	
	count = 1
	directory = './'
	for opt, arg in optlist:
		if opt in ('-h', '--help'):
			show_help(sys.argv[0])
			sys.exit()
		elif opt in ('-c', '--count'):
			count = arg
		elif opt in ('-d', '--output-directory'):
			directory = arg

	try:
		os.chdir(directory)
	except:
		raise
		sys.exit()

	fetch(count)
	print()
