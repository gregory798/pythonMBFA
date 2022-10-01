import random

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

def cherche_et_remplace(motif1, motif2, s):
    if s.find(motif1) != -1:
        s = s.replace(motif1, motif2)
    return s

def lancer_de6():
    return random.randint(1,6)

def moyenne_serie_lancers(n):
    sum = 0
    for i in range(n):
        sum += random.randint(1,6)
    if n >0:
        return sum/n
    else:
        return "Le nombre de lancers doit être positif !"

def frequence_valeur(r,n):
    freq = 0
    for _ in range(n):
        if lancer_de6() == r:
            freq += 1
    return freq/n