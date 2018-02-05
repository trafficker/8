import socket
def __TCP_connect(ip, port_number, delay):
    # Initilize the TCP socket object
    TCP_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCP_sock.settimeout(delay)

    try:
        result = TCP_sock.connect_ex((ip, int(port_number)))

        # If the TCP handshake is successful, the port is OPEN. Otherwise it is CLOSE
        if result == 0:
          print("do")
        else:
         print("fail")

        TCP_sock.close()

    except socket.error as e:

         print("close")
         pass
def main():
    __TCP_connect('www.baidu.com',80,2)

if __name__=='__main__':
    main()