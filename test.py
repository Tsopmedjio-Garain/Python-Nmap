import nmap
nm = nmap.PortScanner()
b = nm.scan('google.com', '22-35')
v = nm.scaninfo()
