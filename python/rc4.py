
# -*- coding: utf-8 -*-

from queue import Queue

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
    
def hash(text):

    digest = [0] * 16 
    for i,x in enumerate(text):
        digest[i%16] = digest[i%16] ^ ord(x)
    
    return digest

key = 'test'
packetQueue = Queue()
rc4 = RC4(key)

class Packet:
    
    def __init__(self, SC, data, type="default"):
        
        # 加密
        text = []
        for i in range(4):
            text.append( chr(SC >> ((3-i))*8) )
        for x in data:
            text.append( x )

        if type!="default" and len(data) < 252:     # 添0
            numZero = 251 - len(data) 
            text += chr(1)
            for _ in range(numZero):
                text += chr(0)

        self.cipher = rc4.encrypt(''.join(text))
        self.HV = hash(text)




class Sender:

    def __init__(self):
        self.SC = 0

    def sendMessage(self, message):
        numSeg = len(message) // 252
        for i in range(numSeg):
            packet = Packet(self.SC, message[i*252 : (i+1)*252])
            self.sendPacket(packet)
        
        packet = Packet(self.SC, message[ numSeg * 252 : ], type="last")
        self.sendPacket(packet)
        
    def sendPacket(self, packet):
        print("[sender] send a packet")
        packetQueue.put(packet)
        self.SC = self.SC + 1


class Receiver:

    def __init__(self):
        self.SC = 0

    def receivePacket(self):
        print()
        print("[receiver] receive a packet")
        packet = packetQueue.get()

        # 解密
        message = rc4.decrypt(packet.cipher)
        
        # 获取SC 
        sc = 0
        for i,x in enumerate(message[0:4]):
            sc = sc + ord(x) << ((3-i)*8)
        print("[receiver] SC : " , sc)
        if sc != self.SC:
            print("the SC is not the same")
            return None

        # hash
        text = list(message)
        digest = hash(text)

        for s, r in zip(packet.HV, digest):
            if s!=r:
                print("the hash value is not the same")
                return None

        self.SC = self.SC + 1

        # 去掉0
        lastIndex = -1
        while message[lastIndex]==chr(0):
            lastIndex -= 1
        
        print("[receiver] message : ")
        if lastIndex != -1:
            print(message[4:lastIndex])
        elif message[lastIndex]==chr(1):
            print(message[4:-1])
        else:
            print(message[4:])


# usage:
#
#   key  :  密钥
#   m   :   message 
#   c   :   cipher 
#   dm  :   decrypted message       

key = 'test'
rc4 = RC4(key)
m = ["helloWorld"] * 100
m = ''.join(m)

sender = Sender()
receiver = Receiver()


# 可以连续地发，也可以发一发，收一收
sender.sendMessage(m)
sender.sendMessage(m)
while not packetQueue.empty():
    receiver.receivePacket()
