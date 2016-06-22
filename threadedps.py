#threaded port scanner
import socket
import threading
from queue import Queue


print_lock = threading.Lock()
server = "pythonprogramming.net"

def pscan(port):
	try:
		con = s.connect((server,port))
		with print_lock:
			print('port ',port, ' is open!')
		con.close()
	except:
		pass

def threader():
	while True:
		worker = q.get()
		pscan(worker)
		q.task_done()

q = Queue()

for x in range(8000):
	t = threading.Thread(target = threader)
	t.daemon = True
	t.start()

for worker in range(1,101):
	q.put(worker)

q.join()


