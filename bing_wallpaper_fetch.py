import urllib.request
import binascii
import json
import wget
import sys
import getopt

images = {}
servers = ['az619822', 'az608707']

#url_pattern='http://www.bing.com/HPImageArchive.aspx?format=js&idx={}&n={}&mkt=en-US'
#
#idx = 0
#while idx < 50:
#	url = url_pattern.format(idx, idx + 16)
#	idx += 1
#
#	try:
#		raw_data = urllib.request.urlopen(url).read().decode('utf-8')
#		image_data = json.loads(raw_data)['images']
#		
#		for i in image_data:
#			date = i['startdate']
#			images[date] = i['url'].split('/')[-1].replace('1920x1080.jpg', '')
#	except:
#		break
#
#print(images)
#
#for date in images:
#	url = 'http://{}.vo.msecnd.net/files/{}'.format(servers[0], images[date])
#	try:
#		filename = wget.download(url + '1920x1200.jpg')
#		print('\nFetched image {}: {}'.format(date, filename))
#	except:
#		try:
#			filename = wget.download(url + '1920x1080.jpg')
#			print('\nFetched image {}: {}'.format(date, filename))
#		except:
#			print('Error getting image from {}: {}'.format(date, url))
#

def fetch(n, directory):
	"""
	Fetch n last images to the given directory
	"""
	pass

def show_help(name):
	print('Usage: python3 {} [OPTIONS]... '.format(name))
	print('Fetch Bing Wallpaper images (according to the Bing\'s API restrictions fetching only the last 16 images is allowed)')
	print('  -c, --count=[COUNT]\t\t\tThe number of images to fetch')
	print('  -o, --output-directory=[DIRECTORY]\tOutput directory to put the images to')

if __name__ == '__main__':	
	args = sys.argv[1:]

	optlist, args = getopt.getopt(args, 'hc:o:', ['help', 'count=', 'output-directory='])
	
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

	fetch(count, directory)
