# LinksGrabber.py - website links grabber
# Created By Best-ITPro, http://best-itpro.ru

# push links to _links.txt file
# push website dump to _dump.txt file

# Grabbing links from web-site


import requests
import time
from bs4 import BeautifulSoup


def main(url, file_dump):
	r = requests.get(url)

	print ('Status: ' + str(r))

	if str(r) != '<Response [200]>':
		return -1

	# Dump to file
	f = open(file_dump, 'w')
	f.write(r.text)
	f.close()


def read_file(file_dump, file_out):

	html = open (file_dump, 'r')
	soup = BeautifulSoup (html, 'lxml')

	links_a =[]
	links = soup.find_all('a')

	f2 = open (file_out, 'w')

	for a in links:
		link = a.get ('href')
		print (link)
		f2.write (link)
		f2.write('\n')
		links_a.append(link)

	f2.close()

# Main program start point
if __name__ == '__main__':

	# Pause (for writing file, secs)
	pause = 1

	http = 'http://'
	url = input ('Input website url: ' + http)

	result = url.find ('.')
	if result == -1:
	    print ("Wrond website: " + url + " , you can try again later..")	
	    exit()		

	linksfile = url + '_links.txt'
	dumpfile = url + '_dump.html'	

	url = http + url

	print ('Open up website: ' + url)	
	
	result = main(url, dumpfile)

	if result == -1:
	    print ("We can't find your website: " + url + " , you can try again later..")	
	    exit()

	time.sleep(pause)

	read_file(dumpfile, linksfile)

	print ('\n\nNow you can find all data in these files: ')
	print ('1. ' + dumpfile + ' - your website dump file')
	print ('2. ' + linksfile + ' - all links from you website')
	print ('\nSee you later ;)\n')

