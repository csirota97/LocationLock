import random

def encrypt(longitude, latitude, msg):
    m2 = ""
    longitude = abs(int(round(longitude,4)*10000))
    latitude = abs(int(round(latitude,4)*10000))
    random.seed(longitude^latitude)

    for c in msg:
        val = ord(c)
        val = val ^ longitude ^ latitude
        longitude = longitude ^ random.randint(0,32767)
        latitude = latitude ^ random.randint(0,32767)
        m2 += chr(val)
    return m2
