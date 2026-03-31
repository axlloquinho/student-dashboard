from main import app
from database import cadastrar
from database import login_funcao
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for


@app.route("/", methods=("GET","POST"))
def rota_login():

    if request.method == "POST":

        nome = request.form['nome']
        senha = request.form['senha']
        
        resultado = login_funcao(nome,senha)
       
        if resultado == "permitido":
            return redirect(url_for("rota_principal", user=nome))

        else:
            return render_template("login.html", invalido="credenciais invalidas")

    return render_template("login.html")


@app.route("/cadastro", methods=("GET","POST"))
def rota_cadastro():

    if request.method == "POST":
        
        nome = request.form['nome']
        senha = request.form['senha']
        
        resultado = cadastrar(nome,senha)

        if resultado == "existe":
            return render_template("cadastro.html",erro=f"usario {nome} ja existe")
    
        return redirect(url_for("rota_principal"))

    return render_template("cadastro.html")    



@app.route("/principal")   
def rota_principal():
    user = request.args.get("user")
    return render_template("principal.html",user=f"{user}")
    

@app.route("/grafico")
def rota_grafico():
  
    return render_template("grafico.html")