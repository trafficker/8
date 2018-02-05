import optparse
import nmap

def  nmapscan(tgtHost, tgtPort):
    nmScan=nmap.PortScanner()
    nmScan.scan(tgtHost,tgtPort)
    # get the port state  
    state=nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
    print(" [*] "+tgtHost+" tcp/"+tgtPort+" "+state)

def main():
        parser = optparse.OptionParser("usage %prog -H <target host> -p <target port>")
        parser.add_option('-H',dest='tgtHost',type = 'string',help = 'specify target host')
        parser.add_option('-p',dest='tgtPort',type ='string',help = 'specify target port[s] separated by comma')
        (options,args)=parser.parse_args()
        tgtHost = options.tgtHost
        tgtPorts = str(options.tgtPort).split(", ")
        if( tgtHost ==None )| ( tgtPorts[0] == None):
            print(parser.usage)
            exit(0)
        for tgtPort in tgtPorts:
          nmapscan(tgtHost,tgtPort)
if __name__ == '__main__':
      main()