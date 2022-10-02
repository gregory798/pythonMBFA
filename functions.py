import random
import math

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

def factorielle(n):
    factorielle = 1
    nb_ops = 0
    for i in range(1, n+1):
        factorielle *= i
        nb_ops += 1
    return factorielle, nb_ops

def combinaisons(n,k):
    n1 = factorielle(n)[0]
    n1_mult = factorielle(n)[1]

    k1 = factorielle(k)[0]
    k1_mult = factorielle(k)[1]

    n_k = factorielle(n-k)[0]
    n_k_mult = factorielle(n-k)[1]

    ans = n1 // (k1*n_k)
    nb_ops = n1_mult + k1_mult + n_k_mult
    return ans, nb_ops

def combis_rapide(n,k):
    prod = 1   
    nb_ops = 0
    for i in range(1, min(k, n - k) + 1):
        prod *= n
        prod //= i
        nb_ops += 2
        n -= 1
    return prod, nb_ops

def nb_plis_fixed(hauteur):
    return math.ceil(math.log(hauteur) / math.log(2))

def nb_plis(epaisseur,hauteur):
    return math.ceil(math.log(hauteur/epaisseur) / math.log(2))

def flechettes(nb_tirs, somme):
    choices = ""
    for x in range(nb_tirs):
        for y in range(nb_tirs):
            if 50*x+20*y == somme and x+y<=nb_tirs:
                z = 10-x-y
                choices += "[50] " * x + "[20] " * y + "[0] " * z + f"<-- SOMME = {somme} <br>"
    return choices

def aire(borne_sup, n):
    nb_point_sous_la_courbe = 0

    for _ in range(n):
        x_axis = random.uniform(0, borne_sup)
        y_axis = random.uniform(0, borne_sup**2)
        if x_axis**2>y_axis:
            nb_point_sous_la_courbe += 1
    
    longueur = borne_sup**2 
    largeur = borne_sup

    aire_approx = longueur*largeur*nb_point_sous_la_courbe/n
    return aire_approx


def liste_moyenne(L):
    return sum(L)/len(L)


def liste_carres(L):
    L_2 = []
    for l in L:
        L_2.append(l**2)
    return L_2

def liste_variance(L):
    return sum(liste_carres(L)) / len(L) - liste_moyenne(L)**2


def liste_produit(L):
    p = 1
    for l in L:
        p *= l
    return p


def entrelacement(L1, L2):
    z = list(zip(L1,L2))
    lst = []

    for elem in z:
        for e in elem:
            lst.append(e)

    return lst

def entrelacement_general(L1, L2):
    reste = []
    if len(L1) < len(L2):
        reste = L2[len(L1):]
    elif len(L1) > len(L2):
        reste = L1[len(L2):]
            
    return entrelacement(L1, L2) + reste


def somme_chaine(s):
    try:
        lst = s.split(" ")
        lst_int = (int(l) for l in lst)
        return sum(lst_int)
    except Exception as e:
        return f"Erreur : {e}"