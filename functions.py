def conv_sec(h, m, s):
    return h*3600 + m *60 + s

def bonjour(n):
    if n == 1:
        return "Bonjour, Monsieur"
    elif n == 2:
        return "Bonjour, Madame"
    else:
        return "Bonjour"

def bissextile(a):
    return (a%400==0) or (a%4==0 and a%100!=0)

def decompose_chaine(s):
    alpha = ""
    num = ""

    for i in s:
        if i.isalpha():
            alpha+=i
        elif i.isnumeric():
            num+=str(i)

    if not num:
        return alpha, ""
    else:
        return alpha, int(num)