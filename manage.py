from flask import Flask,request,render_template,jsonify
import json
app=Flask(__name__)
@app.route('/')
def render():
          return render_template('menu.html')
@app.route('/d',methods=['POST'])
def dados():
        dados={

        'nome':request.form['nome'],
        'genero':request.form['genero'],
        'instagram':request.form['instagram'],
        'idade':request.form['idade']
}
        try:
                with open ("dados/pesquisa.json","r") as arq:
                     lista_dados=json.load(arq)
        except FileNotFoundError:
                lista_dados=[]
        lista_dados.append(dados)
        with open("dados/pesquisa.json","w") as arq:
                json.dump(lista_dados,arq,indent=4)
        return render_template('resultados.html')
if __name__=='__main__':
        app.run(debug=True)