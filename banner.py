
#coding=utf-8  
import socket
def retBanner(ip,port):
    try:
        socket.setdefaulttimeout(3)
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.setblocking(0)
        s.connect_ex((ip,port))
        #banner=s.recv(1)
        return "bad"

    except:
        return " 连不上 "
def checkVulns(banner):
    if'vsFTPd'in banner:
        print('[+] vsFTPd is vulnerable.')
    elif'FreeFloat Ftp Server'in banner:
        print('[+] FreeFloat Ftp Server is vulnerable.')
    else:
        print('[-] FTP Server is not vulnerable.')
    return
def main():
    ips=['www.baidu.com','127.0.0.1']
    port=9009
    banner1=retBanner('www.baidu.com',port)
    if banner1:
        print('[+] '+ips[0]+": "+banner1.strip('\n'))
        checkVulns(banner1)
    banner2=retBanner(ips[1],port)
    if banner2:
        print('[+] '+ips[1]+": "+banner2.strip('\n'))
        checkVulns(banner2)
if __name__=='__main__':
    main()