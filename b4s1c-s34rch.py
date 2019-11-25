#!/usr/bin/env/python
# create by b3r0d4y
import shodan
import sys
import pyfiglet


banner = pyfiglet.figlet_format("sh0d4n Sc4Nn3r")
creator = pyfiglet.figlet_format("Cr34t0r : b3r0d4y", font = "digital")
print  banner
print creator

#Conf

api_key = "THIS IS YOUR API KEY"

#input

if len(sys.argv) == 1:
	print 'Usage: %s <search query>' % sys.argv[0]
	sys.exit(1)
try:
	print('\x1b[6;30;42m' + 'Search Success Please Wait Results !' + '\x1b[0m')
	#setup the api
	api = shodan.Shodan(api_key)
	
	#Perform the search
	query = ' '.join(sys.argv[1:])
	result = api.search(query)

	#loop n print each ip etc.
	for service in result['matches']:
		print "-" * 30
		print "Organization Name: ",service['org']
		print "-" * 30
		print "IP Address: ", service['ip_str']
		print "-" * 30
		print "Port Number: ", service['port']
except Exception as e :
	print '\x1b[6;20;41m' + 'Error!!!' + '\x1b[0m'
	print '\x1b[6;20;41m' + 'Please use correct format or change search input ! ' + '\x1b[0m'
	sys.exit(1)
