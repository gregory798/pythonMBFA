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