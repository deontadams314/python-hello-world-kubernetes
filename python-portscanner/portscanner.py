import argparse 
import socket
from socket import *
"""
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))
"""

def conn_scan(host, port):
	try:
		connSkt = socket(AF_INET, SOCK_STREAM)
		connSkt.conect((host,port))
		connSkt.send('ViolentPython')
		results = connSkt.recv(100)
		print ('[+]{}/tcp open'.format(port))
		connSkt.close()
	except:
		print('[-]{}/tcp closed'.format(port))


def port_scan(tgtHost, tgtPorts):
	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		print ("[-] Cannot resolve '{}': Unknown host".format(tgtHost))
		return
	try:
		tgtName = gethostbyaddr(tgtIP)
		print ('[+] Scan Results for: {}'.format(tgtName[0]))
	except:
		print ('[+] Scan Results for: {}'.format(tgtIP))
		setdefaulttimeout(1)
	#for tgtPort in tgtPorts:
	print('Scanning port {}'.format(tgtPorts))
	conn_scan(tgtHost, int(tgtPorts))

if __name__ == '__main__':
	port_scan('youtube.com',3389)