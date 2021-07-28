from pyDes import *
import base64
V0 = [102, 67, 119, 112, 103, 86, 72, 55, 124, 88, 93, 74, 85, 56, 37, 107, 95, 114, 127, 124, 65, 124, 102, 78, 76, 106, 106, 105, 40, 36, 93, 115]
def DeCheck(str):
    v1 = []
    for i in range(len(str)):
        v1.append(chr(str[i] ^ i))
    xx = "".join(v1)
    return xx

if __name__ == '__main__':
    key = 'poi7y6gt'
    iv = '\x01\x02\x03\x04\x05\x06\x07\x08'
    k = des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    flag = k.decrypt(base64.b64decode(DeCheck(V0)))
    print("Your flag is: " +  flag.decode())
