#KSA

def KSA(key):
    if type(key) == str:
        key = [ord(x) for x in key]

    S = [i for i in range(256)]
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    
    return S

#PRGA
def PRGA(S, roun, j):
    for r in range(roun):
        for i in range(256):
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]
        r =r+1
    
    return (S, j)

def IPRGA(S, roun, j):
    i = 0
    for r in range(roun):
        for _ in range(256):
            S[i], S[j] = S[j], S[i]
            j = (j - S[i]) % 256
            i = (i - 1) % 256
        r =r+1

    return (S, j)

key = "test"
S = KSA(key)
initialS = S.copy()

print("initial S")
print()
print(S)
print()

round = 10

S, j = PRGA(S, round, 0)
print("forward ", round, " rounds")
print()
print(S)
print()

S, j = IPRGA(S, round, j)
print("backward ", round, " rounds")
print()
print(S)
print()

print("The same as the initial one ? ", initialS==S)