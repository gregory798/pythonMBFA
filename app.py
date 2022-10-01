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

@app.route('/td2/exercice1')
def td2e1():
    return render_template('td2e1.html')

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
                    return f"{func.combinaisons(n,k)[0]} ({func.combinaisons(n,k)[1]}) multiplications"
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
                    return f"{func.combis_rapide(n,k)[0]} ({func.combis_rapide(n,k)[1]}) opérations"
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
            print(horaires)
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