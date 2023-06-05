s  = " "


def getP(s: str) -> bool:
    w = ""
    for i in range(len(s) - 1):
        if (ord(s[i]) >= 65 and ord(s[i]) <= 90) or (ord(s[i]) >= 97 and ord(s[i]) <= 122):
            w += s[i]
    w = w.upper()
    return w

a = getP(s)

def validP(a):
    t = a
    l = 0
    r = len(t) - 1
    while l <= r:
        if t[l] != t[r]:
            return False
        return True

    
b = validP(a)
print(b)
