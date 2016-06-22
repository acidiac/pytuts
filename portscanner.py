import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "twitter.com"

def pscan(port):
	try:
		s.connect((server,port))
		return True
	except:
		return False

for x in range(1,100):
	if pscan(x):
		print('port ',x,' is open')


