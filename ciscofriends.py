import socket
import re
import time

IPP = []

def IPLIST():

    try:
        with open("iplist", "r") as IP:
            for line in IP.readlines():
                line = line.rstrip("\n")
                if not line:
                    continue
                IPP.append(line)
        IP.close()
        
    except:
        print("list read error ")
       
def testy():
        
    for target in IPP:

        try:
            telsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            telsock.connect((target, 23))
            print(telsock.recv(1024))                
        except:
            print("")
                        
        try:
            datpass = re.findall(r"Password\:", str(telsock.recv(1024)), flags=re.MULTILINE)
            datname = re.findall(r"Username\:", str(telsock.recv(1024)), flags=re.MULTILINE)
            loggedin = re.findall(r"[\[\]\^\$\.\|\?\*\+\(\)\\~`\!@#%&\-_+={}'""<>:;, ]{1,}", str(telsock.recv(1024)), flags=re.MULTILINE)
            time.sleep(5)
            
            try:
                if datname:
                    sendn = ("cisco\n")
                    telsock.send(sendn)
                    time.sleep(1)
                else:
                    print("")

            except:
                print("")

            try:
                if datpass:
                    sendp = ("cisco\n")
                    telsock.send(sendp)
                    time.sleep(1)
                else:
                    print("")
            except:
                print("")
                
            time.sleep(1)
            print(telsock.recv(1024))

            try:
                if loggedin:
                        print("logged in to " , target)
                        wait(3)
                        print(telsock.recv(1024))
                else:
                        print("")
            except:
                    print("")
                
            time.sleep(1)
            print(telsock.recv(1024))

        except:
            print("")

IPLIST()
testy()
