from flask import Flask, render_template, redirect, request, flash
import json


app=Flask(__name__)
app.config['SECRET_KEY'] = 'MATHEUSB'


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():

    nome = request.form.get('nome')    
    senha = request.form.get('senha')
   
    with open('usuarios.json') as usuariosTemp:
        usuario = json.load(usuariosTemp)
        cont = 0
        for usuario in usuario:
            cont += 1
            if usuario['nome'] == nome and usuario['senha'] == senha:
                return render_template("homeusuario.html")
            if cont >= len(usuario):
                flash('USUÁRIO OU SENHA INVÁLIDO')
                return redirect("/")

    # if nome == "matheus" and senha == "1234":
    #     return render_template("homeusuario.html")
    # else:
    #     flash('USUÁRIO ou SENHA INVÁLIDOS')
    #     return redirect('/')


if __name__ in "__main__":
    app.run(debug=True)


    