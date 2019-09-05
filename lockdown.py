import encrypt as e
import geocoder as g
import threading, time, os, socket
from getpass import getpass
import sys
sys.argv.pop(0)

try:
    os.system("clear")
except:
    os.system("cls")

msg = ""
longitude = ""
latitude = ""
wrong = False

password = getpass()


def connect():
    global longitude, latitude, wrong
    '''
    client, addr = s.accept()

    print(f"Connection from {addr} has been established")
    '''
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('',17388))
    msg_size = s.recv(3)
    msg_size = int(msg_size.decode('utf-8'))
    msg = s.recv(msg_size).decode('utf-8')
    p = msg.split('/')[0]
    k = int(float(msg.split('/')[3]))
    try:
        for i in range(len(p)):
            if ord(p[i])^k != ord(password[i]):
            #if p[i] != password[i]
                print("Password does not match\nExiting now")
                wrong = True
                return
    except:
        print("Password does not match\nExiting now")
        wrong = True
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

        if wrong == True:
            exit(-1)
        else:
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
    
    if wrong == True:

        exit(-1)
    else:
        try:
            os.system("clear")
        except:
            os.system("cls")


t = threading.Thread(target = connect, name = "connect")
t2 = threading.Thread(target = waiting, name = "wait")

def main():
    try:
        client = None
        addr = ""

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(('',17389))


        t.start()
        t2.start()

        #print("connecting".upper())
        t.join()
        t2.join()


        if wrong == True:
            return
        
        if len(sys.argv) == 0:
            file_name = input("file name:\n>\t")
            arg = False    
        

            with open(file_name) as f:
                msg = e.encrypt(longitude, latitude, f.read())

            option = input("(E)ncrypt or (D)ecrypt:\n>\t")

            if option.upper() == 'D':
                file_name = file_name[:file_name.index('.')]+'_decrypted' + file_name[file_name.index('.'):]

            with open(file_name, 'w') as f:
                f.write(msg)
        else:
            option = input("(E)ncrypt or (D)ecrypt:\n>\t")

            while len(sys.argv) > 0:
                file_name = sys.argv.pop(0)
        

                with open(file_name) as f:
                    msg = e.encrypt(longitude, latitude, f.read())


                if option.upper() == 'D':
                    file_name = file_name[:file_name.index('.')]+'_decrypted' + file_name[file_name.index('.'):]

                with open(file_name, 'w') as f:
                    f.write(msg)
    except:
        try:
            os.system("clear")
        except:
            os.system("cls")

        print("ERROR\nExiting now")


main()
