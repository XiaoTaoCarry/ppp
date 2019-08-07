
# -*- coding: utf-8 -*-

class RC4:

    def __init__(self, key):
        key = [ord(x) for x in key] 

        # 计算S 
        S = [i for i in range(256)]
        keylen = len(key)
        T = [key[i % keylen] for i in range(256)]

        # 计算 i, j
        j = 0
        for i in range(256):
            j = (j + S[i] + key[i % len(key)]) % 256 
            S[i], S[j] = (S[j], S[i]) 
        
        self.encryptS = S
        self.decryptS = S.copy() 
        self.k = []
        self.key = key

    def genKeyStream(self, length, type="en"):
        S = None
        if type=="de":
            S = self.decryptS
        else:
            S = self.encryptS

        i = 0
        j = 0
        k = []
        for _ in range(length):
            i = (i+1) % 256
            j = (j + S[i]) % 256 
            S[i], S[j] = (S[j], S[i])
            t = (S[i] + S[j]) % 256 
            k.append(S[t])
        
        self.k = k

    def encrypt(self, message):
        msg = [ord(c) for c in message]

        # 产生密钥流 
        self.genKeyStream(len(msg))
        rtn = [ char ^ mask for char, mask in zip(msg, self.k) ]
        return rtn

    def decrypt(self, cipher):
        # cipher 是列表

        self.genKeyStream(len(cipher), type="de")

        rtn = [ char ^ mask for char, mask in zip(cipher, self.k) ]
        rtn = [ chr(x) for x in rtn]
        return ''.join(rtn)
    


# usage:
#
#   key  :  密钥
#   m   :   message 
#   c   :   cipher 
#   dm  :   decrypted message       

key = 'test'
rc4 = RC4(key)
m = "hello world"
c = rc4.encrypt(m)
print(c)

dm = rc4.decrypt(c) 
print(dm)

