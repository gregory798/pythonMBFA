from flask import Flask, render_template, request
import re, math
import functions as func


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/td1')
def td1():
    return render_template('td1.html')


@app.route('/td2')
def td2():
    return render_template('td2.html')

@app.route('/td3')
def td3():
    return render_template('td3.html')

@app.route('/td3/exercice1')
def td3e1():
    return render_template('td3e1.html')

@app.route('/td3/exercice2')
def td3e2():
    return render_template('td3e2.html')

@app.route('/td3/exercice4')
def td3e4():
    return render_template('td3e4.html')


@app.route('/td3/exercice4/somme')
def td2e4somme():
    try:
        q = request.args.get("q")
        return str(func.somme_chaine(q))
    except Exception as e:
        return f"Erreur : {e}"

@app.route('/td3/exercice1/moyenne')
def td2e1moyenne():
    try:
        q = request.args.get("q")
        lst = q.split(",")
        try:
            lst_moyenne = []
            for l in lst:
                lst_moyenne.append(float(l))
            return str(func.liste_moyenne(lst_moyenne))
        except Exception as e:
            return f"Erreur : {e}"
    except Exception as e:
        return f"Erreur : {e}"

@app.route('/td3/exercice1/variance')
def td2e1variance():
    try:
        q = request.args.get("q")
        lst = q.split(",")
        try:
            lst_variance = []
            for l in lst:
                lst_variance.append(float(l))
            return str(func.liste_variance(lst_variance))
        except Exception as e:
            return f"Erreur : {e}"
    except Exception as e:
        return f"Erreur : {e}"

@app.route('/td3/exercice2/produit')
def td2e2produit():
    try:
        q = request.args.get("q")
        lst = q.split(",")
        try:
            lst_produit= []
            for l in lst:
                lst_produit.append(float(l))
            return str(func.liste_produit(lst_produit))
        except Exception as e:
            return f"Erreur : {e}"
    except Exception as e:
        return f"Erreur : {e}"

@app.route('/td3/exercice3', methods=['GET', 'POST'])
def td3e3():
    if "submit_ex_3_1" in request.form:
        e1l1 = request.form.get("e1l1")
        e1l2 = request.form.get("e1l2")
        lst1 = e1l1.split(",")
        lst2 = e1l2.split(",")


        try:
            L1= []
            for l in lst1:
                L1.append(int(l))
            L2= []
            for l in lst2:
                L2.append(int(l))

            ret_lst = str(func.entrelacement(L1, L2))
            return render_template('td3e3.html', ans1=ret_lst, ans2="(rentrez des listes ci-dessus)")
        except Exception as e:
            return render_template('td3e3.html', ans1=f"Erreur : {e}", ans2="(rentrez des listes ci-dessus)")


    elif "submit_ex_3_2" in request.form:
        e2l1 = request.form.get("e2l1")
        e2l2 = request.form.get("e2l2")
        lst1 = e2l1.split(",")
        lst2 = e2l2.split(",")
        try:
            L1= []
            for l in lst1:
                L1.append(int(l))
            L2= []
            for l in lst2:
                L2.append(int(l))

            ret_lst = str(func.entrelacement_general(L1, L2))
            return render_template('td3e3.html', ans1="(rentrez des listes ci-dessus)", ans2=ret_lst)
        except Exception as e:
            return render_template('td3e3.html', ans1="(rentrez des listes ci-dessus)", ans2=f"Erreur : {e}")
    else:
        return render_template('td3e3.html', ans1="(rentrez des listes ci-dessus)", ans2="(rentrez des listes ci-dessus)")

@app.route('/td4')
def td4():
    return render_template('td4.html')


@app.route('/td4/exercice1')
def td4e1():
    return render_template('td4e1.html')

@app.route('/td4/exercice1/nb_max')
def td4e1nb_max():
    try:
        q = request.args.get("q")
        lst = q.split(",")
        try:
            lst_nb_max= []
            for l in lst:
                lst_nb_max.append(int(l))
            return str(func.nb_max(lst_nb_max))
        except Exception as e:
            return f"Erreur : {e}"
    except Exception as e:
        return f"Erreur : {e}"

@app.route('/td4/exercice2')
def td4e2():
    return render_template('td4e2.html')

@app.route('/td4/exercice3', methods=['GET', 'POST'])
def td4e3():
    dic = ""
    if "submit_file" in request.form:
        file = request.files["file"]
        text = file.read().decode('utf-8')
        freqs = func.freqs_lettres(text)
        return render_template('td4e3.html', dic=freqs)

    return render_template('td4e3.html', dic=dic)

@app.route('/td4/exercice3/freqs')
def td4e3freqs():
    try:
        q = request.args.get("q")
        return str(func.freqs_lettres(q))
    except Exception as e:
        return f"Erreur : {e}"

@app.route('/td4/exercice2/dispo1')
def td4e2dispo1():
    try:
        q = request.args.get("q")
        prod_prix = q.split(",")
        try:
            prod= prod_prix[0]
            prix= float(prod_prix[1])
            return str(func.disponibilite1(prod, prix))
        except Exception as e:
            return f"Erreur : {e}"
    except Exception as e:
        return f"Erreur : {e}"

@app.route('/td4/exercice2/dispo2')
def td4e2dispo2():
    try:
        q = request.args.get("q")
        prod_prix = q.split(",")
        try:
            prod= prod_prix[0]
            prix= float(prod_prix[1])
            return str(func.disponibilite2(prod, prix))
        except Exception as e:
            return f"Erreur : {e}"
    except Exception as e:
        return f"Erreur : {e}"

@app.route('/td4/exercice2/prix_moyen')
def td4e2prix_moyen():
    prix = func.generate_dic()
    return str(func.prix_moyen(prix))


@app.route('/td4/exercice2/tous_dispo')
def td4e2tous_dispo():
    prix = func.generate_dic()
    panier = func.generate_cart()
    return str(func.tous_dispos(panier, prix))


@app.route('/td4/exercice2/fourchette')
def td4e2fourchette():
    try:
        q = request.args.get("q")
        mini_maxi = q.split(",")
        try:
            mini = float(mini_maxi[0])
            maxi = float(mini_maxi[1])
            prix = func.generate_dic()
            return str(func.fourchette_prix(mini, maxi, prix))
        except Exception as e:
            return f"Erreur : {e}"
    except Exception as e:
        return f"Erreur : {e}"


@app.route('/td2/exercice2', methods=['GET', 'POST'])
def td2e2():
    if "submit_ex_2" in request.form:
        motif1 = request.form.get("motif1")
        motif2 = request.form.get("motif2")
        s = request.form.get("s")
        s = func.cherche_et_remplace(motif1, motif2, s)
        return render_template('td2e2.html', ans=s)
    else:
        return render_template('td2e2.html', ans="(entrez une valeur ci-dessus)")

@app.route('/td2/exercice3')
def td2e3():
    return render_template('td2e3.html')

@app.route('/td2/exercice4')
def td2e4():
    return render_template('td2e4.html')

@app.route('/td2/bonus1')
def td2b1():
    return render_template('td2b1.html')

@app.route('/td2/bonus1/hauteur')
def td2b1hauteur():
    try:
        q = int(request.args.get("q"))
        return str(func.nb_plis_fixed(q))
    except Exception as e:
        return f"Erreur : {e}"

@app.route('/td2/bonus1/epaisseur')
def td2b1epaisseur():
    try:
        q = request.args.get("q")
        r = re.compile('.*/.*')
        if r.match(q) is not None:
            eh = q.split("/")
            try:
                e = float(eh[0])
                h = float(eh[1])
                return str(func.nb_plis(e, h))
            except:
                return "Veuillez entrer des nombres uniquement !"
        else:
            return "Format : &lt;float&gt;/&lt;float&gt; (Ex : 0.1/324 000)"
    except Exception as e:
        return f"Erreur : {e}"

@app.route('/td2/bonus2/flechettes')
def td2b2flechettes():
    try:
        q = request.args.get("q")
        r = re.compile('.*,.*')
        if r.match(q) is not None:
            ns = q.split(",")
            try:
                n = int(ns[0])
                s = int(ns[1])
                return func.flechettes(n,s)
            except:
                return "Veuillez entrer des entiers uniquement !"
        else:
            return "Format : &lt;int&gt;,&lt;int&gt; (Ex : 10,300)"
    except Exception as e:
        return f"Erreur : {e}"


@app.route('/td2/bonus2/aire')
def td2b2aire():
    try:
        q = request.args.get("q")
        r = re.compile('.*,.*')
        if r.match(q) is not None:
            bn = q.split(",")
            try:
                b = float(bn[0])
                n = int(bn[1])
                return str(func.aire(b, n))
            except:
                return "Veuillez entrer des nombres uniquement !"
        else:
            return "Format : &lt;float&gt;,&lt;int&gt; (Ex : 1,10000)"
    except Exception as e:
        return f"Erreur : {e}"

@app.route('/td2/bonus2')
def td2b2():
    return render_template('td2b2.html')


@app.route('/td2/bonus3')
def td2b3():
    return render_template('td2b3.html')

@app.route('/td2/exercice4/factorielle')
def td2e4factorielle():
    try:
        q = int(request.args.get("q"))
        ans = func.factorielle(q)[0]
        nb_ops = func.factorielle(q)[1]
        return f"{ans} ({nb_ops} opérations)"
    except Exception as e:
        return f"Erreur : {e}"

@app.route('/td2/exercice4/combinaisons')
def td2e4combinaisons():
    try:
        q = request.args.get("q")
        r = re.compile('.*,.*')
        if r.match(q) is not None:
            nk = q.split(",")
            try:
                n = int(nk[0])
                k = int(nk[1])
                if k > n:
                    return "k ne peut être supérieur à n !"
                else:
                    return f"{func.combinaisons(n,k)[0]} ({func.combinaisons(n,k)[1]} multiplications)"
            except:
                return "Veuillez entrer des entiers uniquement !"
        else:
            return "Format : &lt;int&gt;,&lt;int&gt; (Ex : 5,3)"
    except Exception as e:
        return f"Erreur : {e}"


@app.route('/td2/exercice4/combis_rapide')
def td2e4combis_rapide():
    try:
        q = request.args.get("q")
        r = re.compile('.*,.*')
        if r.match(q) is not None:
            nk = q.split(",")
            try:
                n = int(nk[0])
                k = int(nk[1])
                if k > n:
                    return "k ne peut être supérieur à n !"
                else:
                    return f"{func.combis_rapide(n,k)[0]} ({func.combis_rapide(n,k)[1]} opérations)"
            except:
                return "Veuillez entrer des entiers uniquement !"
        else:
            return "Format : &lt;int&gt;,&lt;int&gt; (Ex : 5,3)"
    except Exception as e:
        return f"Erreur : {e}"

@app.route('/td2/exercice3/lancer_de')
def td2e3lancer_de():
    return str(func.lancer_de6())

@app.route('/td2/exercice3/moyenne')
def td2e3moyenne():
    try:
        q = int(request.args.get("q"))
        return str(func.moyenne_serie_lancers(q))
    except Exception as e:
        return f"Erreur : {e}"

@app.route('/td2/exercice3/rn')
def td2e3rn():
    try:
        q = request.args.get("q")
        r = re.compile('.*,.*')
        if r.match(q) is not None:
            rn = q.split(",")
            try:
                r = int(rn[0])
                n = int(rn[1])
                return str(func.frequence_valeur(r,n))
            except:
                return "Veuillez entrer des entiers uniquement !"
        else:
            return "Format : &lt;int&gt;,&lt;int&gt; (Ex : 5,2365)"
    except Exception as e:
        return f"Erreur : {e}"

@app.route('/td1/exercice1')
def td1e1():
    return render_template('td1e1.html')

@app.route('/td1/exercice2')
def td1e2():
    return render_template('td1e2.html')

@app.route('/td1/exercice3')
def td1e3():
    return render_template('td1e3.html')

@app.route('/td1/exercice4')
def td1e4():
    return render_template('td1e4.html')

@app.route('/td1/exercice5')
def td1e5():
    return render_template('td1e5.html')

@app.route('/td1/exercice6')
def td1e6():
    return render_template('td1e6.html')

@app.route('/td2/exercice1/s')
def td2e1s():
    q = request.args.get("q")
    return str(func.decompose_chaine(q))

@app.route('/td1/exercice6/bonjour')
def td1e5bonjour():
    q = int(request.args.get("q"))
    return str(func.bonjour(q))

@app.route('/td1/exercice6/bissextile')
def td1e5bissextile():
    q = int(request.args.get("q"))
    return str(func.bissextile(q))

@app.route('/td1/exercice5/heure')
def td1e5heure():
    q = request.args.get("q")
    r = re.compile('.*:.*:.*')
    if r.match(q) is not None:
        xyz = q.split(":")
        try:
            x = int(xyz[0])
            y = int(xyz[1])
            z = int(xyz[2])
            return str(func.conv_sec(x, y, z))
        except Exception as e:
            return f"Erreur :<br>{e}"
    else:
        return "Format : &lt;int&gt;:&lt;int&gt;:&lt;int&gt; (Ex : 10:10:10)"

@app.route('/td1/exercice5/delta')
def td1e5delta():
    q = request.args.get("q")
    r = re.compile('.*:.*:.*-.*:.*:.*')
    if r.match(q) is not None:
        horaires = q.split(":")
        try:
            h1 = int(horaires[0])
            m1 = int(horaires[1])
            s1 = int(horaires[2].split("-")[0])
            h2 = int(horaires[2].split("-")[1])
            m2 = int(horaires[3])
            s2 = int(horaires[4])
            return str(func.conv_sec(h1, m1, s1) - func.conv_sec(h2, m2, s2))
        except Exception as e:
            return f"Erreur :<br>{e}"
    else:
        return "Format : &lt;int&gt;:&lt;int&gt;:&lt;int&gt;-&lt;int&gt;:&lt;int&gt;:&lt;int&gt; (Ex : 10:10:10-05:05:05)"

@app.route('/td1/exercice4/livres')
def td1e4livres():
    q = int(request.args.get("q"))
    book_price = 24.95 - (24.95 * 40/100)
    delivery_price = 3
    delivery_reduced_price = 0.75
    if q < 1:
        return "0 €"
    elif q == 1:
        return f"{book_price + delivery_price } €"
    else:
        total_price = q * book_price + delivery_price + delivery_reduced_price * (q-1)
        return f"{round(total_price)} €"

@app.route('/td1/exercice4/volume')
def td1e4volume():
    q = request.args.get("q")
    return str((4/3) * math.pi * int(q)**3)

@app.route('/td1/exercice3/couleur')
def td1e3couleur():
    q = request.args.get("q")
    bounds = q + (" " + q)*(len(q*2)-2) + " " + q
    middle = q + " " + ((" "* len(q)) + " ") * (len(q*2)-2) + q
    mid = ""
    for _ in range(len(q)-2):
        mid += middle + "\n"
    ret = bounds + "\n" + mid + bounds
    return ret

@app.route('/td1/exercice1/minutes')
def td1e1minutes():
    q = request.args.get("q")
    r = re.compile('.*:.*')
    if r.match(q) is not None:
        xy = q.split(":")
        try:
            x = int(xy[0])
            y = int(xy[1])
            return str(x*60 + y)
        except Exception as e:
            return f"Erreur :<br>{e}"
    else:
        return "Format : &lt;int&gt;:&lt;int&gt; (Ex : 42:42)"


@app.route('/td1/exercice1/miles')
def td1e1miles():
    q = float(request.args.get("q"))
    try:
        return str(round((q/1.61), 5))
    except Exception as e:
        return f"Erreur :<br>{e}"

    

@app.route('/base')
def base():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True)