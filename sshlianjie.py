import pexpect

PROMPT = ['# ', '>>> ', '> ', "\$ "]


def send_command(child, cmd):
    child.sendline(cmd)
    child.expect(PROMPT)
    print(child.before)


def connect(user, host, password):
    ssh_newkey = 'are you sure you want to continue connecting'
    conn_info = 'ssh ' + user + '@' + host
    child = pexpect.spawn(conn_info)#windows wu spawn
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword:'])
    if ret == 0:
        print('[-] error connecting')
        return

    if ret == 1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword:'])

        if ret == 0:
            print('[-] error connecting')
            return

        child.sendline(password)
        child.expect(PROMPT)
        return child


def main():
    host = 'localhost'
    user = 'root'
    password = 'toor'

    child = connect(user, host, password)
    send_command(child, 'cat /etc/shadow | grep root')


if __name__ == '__main__':
    main()