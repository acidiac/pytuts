import webbrowser
import time

n = 0
while n<3:
	print(time.ctime())
	time.sleep(3)
	webbrowser.open("http://stackoverflow.com/questions/20831043/console-within-sublime-text")
	n+=1