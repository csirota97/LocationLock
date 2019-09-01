import encrypt as e
import geocoder as g
import threading, time, os, socket
from getpass import getpass

try:
    os.system("clear")
except:
    os.system("cls")

msg = ""
longitude = ""
latitude = ""

password = getpass()


def connect():
    global longitude, latitude
    '''
    client, addr = s.accept()

    print(f"Connection from {addr} has been established")
    '''
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('',17388))
    msg_size = s.recv(3)
    print(msg_size)
    msg_size = int(msg_size.decode('utf-8'))
    msg = s.recv(msg_size).decode('utf-8')
    print("\n"+msg)
    p = msg.split('/')[0]
    k = int(float(msg.split('/')[3]))
    try:
        for i in range(len(p)):
            if ord(p[i])^k != ord(password[i]):
            #if p[i] != password[i]
                print("Password does not match\nExiting now")
                exit(-1)
    except:
        print("Password does not match\nExiting now")
        exit(-1)

    longitude = float(msg.split('/')[1])
    latitude = float(msg.split('/')[2])


    

def waiting():
    c = ["connecting\r","connecting.\r","connecting..\r","connecting...\r"]
    while t.is_alive():

        for i in c:
            if not t.is_alive():
                break
            print(i, end = "")
            time.sleep(.5)


        try:
            os.system("clear")
        except:
            os.system("cls")
        

        '''
        print("connecting", end="")
        if t.isAlive():
            time.sleep(.5)
            print(".",end="")
        else:
            break
        if t.isAlive():
            time.sleep(.5)
            print(".", end="")
        else:
            break
        if t.isAlive():
            time.sleep(.5)
            print(".", end="")
        else:
            break

        time.sleep(.5)

        print()
        '''

    time.sleep(.5)
    
    try:
        os.system("clear")
    except:
        os.system("cls")
    

t = threading.Thread(target = connect, name = "connect")
t2 = threading.Thread(target = waiting, name = "wait")

client = None
addr = ""

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('',17389))


t.start()
t2.start()

#print("connecting".upper())
t.join()
t2.join()

file_name = input("file name:\n>\t")

with open(file_name) as f:
    msg = e.encrypt(longitude, latitude, f.read())

file_name = file_name[:file_name.index('.')]+'_decrypted' + file_name[file_name.index('.'):]

with open(file_name, 'w') as f:
    f.write(msg)
