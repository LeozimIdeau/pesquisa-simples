from flask import Flask,request,render_template,jsonify
import json
app=Flask(__name__)
@app.route('/')
def render():
          return render_template('menu.html')
@app.route('/d',methods=['POST'])
def dados():
        generos=['mulher','homem','feminino','masculino','m','f','h']
        genero=request.form.get('genero')
        nome=request.form.get('nome')
        insta=request.form.get('instagram')
        idade=request.form.get('idade')
        dados={

                  'nome':nome,
                  'genero':genero,
                  'instagram':insta,
                  'idade':idade
                }
        if genero in generos:
            try:
                with open ("dados/pesquisa.json","r") as arq:
                     lista_dados=json.load(arq)
            except FileNotFoundError:
                lista_dados=[]
            lista_dados.append(dados)
            with open("dados/pesquisa.json","w") as arq:
                json.dump(lista_dados,arq,indent=4)
            return render_template('resultados.html')
        else:  
            return render_template('menu.html')          
if __name__=='__main__':
        app.run(debug=True)