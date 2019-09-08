import random, traceback

def encrypt(longitude, latitude, msg):

    m2 = ""
    longitude = abs(int(round(longitude,4)*10000)) % 0x10000
    latitude = abs(int(round(latitude,4)*10000)) % 0x10000
    
    print(longitude, latitude)

    try:
        for c in msg:
            val = ord(c)
            val = val ^ (longitude ^ latitude)
            m2 += chr(val)
    except Exception as err:
        traceback.print_exc()
        print(c, ord(c), val)

    return m2
