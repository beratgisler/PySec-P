import nmap
import pyfiglet

# banner icin pyfiglet

ascii_banner = pyfiglet.figlet_format("b3r0 Scanner")
print(ascii_banner)

print("Please wait for finishing the scan :))")

#ip degistir-port degistir
Chest_Scan = nmap.PortScanner()
Chest_Scan.scan('rootcon.com.tr', '0-1000')

# loop ekran-cikti

for host in Chest_Scan.all_hosts():
    print('----------------------------------------------------')
    print('Host : {} ({})'.format(host, Chest_Scan[host].hostname()))
    print('State : {}'.format(Chest_Scan[host].state()))
    for proto in Chest_Scan[host].all_protocols():
        print('----------')
        print('Protokol : {}'.format(proto))
 
        lport = Chest_Scan[host][proto].keys()
        for port in lport:
            print ('port : {}\tstate : {}'.format(port, Chest_Scan[host][proto][port]['state']))
