import optparse
from socket import *
from threading import*
screenLock=Semaphore(value=1)
def connScan(tgtHost,tgtPort):
    try:
        connSkt=socket(AF_INET,SOCK_STREAM)
        connSkt.connect((tgtHost,tgtPort))
        connSkt.send('VioletPython\r\n')
        results=connSkt.recv(100)
        screenLock.acquire()
        print('[+]%d/tcp open'% tgtPort)
        print('[+]'+str(results))
    except:
        screenLock.acquire()
        print('[-]%d/tcp closed'%tgtPort)
    finally:
        screenLock.release()
        connSkt.close()

def portScan(tgtHost,tgtPorts):
    try:
        tgtIP=gethostbyname(tgtHost)
    except:
        print("[-]Cannot resolve '%s':Unknown host"%tgtHost)
        return
    try:
        tgtName=gethostbyaddr(tgtIP)
        print('\n[+]Scan Results for:'+tgtName[0])
    except:
        print('\n[+]Scan Results for:'+tgtIP)
