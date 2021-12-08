from flask import Flask

app = Flask(__name__)


# porta padrão 5000
@app.route('/')
def index():
    return 'Fala, moça. Primeira janelinha, muito doido isso aqui'

# para não dar erro caso não tenha algum nome
@app.route('/teste', defaults={'nome': None})
@app.route('/teste/<nome>')
def teste(nome):
    if nome:
        return f"Hey,{nome}!"
    else:
        return 'Olá!'


# para trocar o tipo do retorno str --> int)
@app.route('/teste/tipo/<int:id_>')
def teste2(id_):
    return f'Agora {id_} é um inteiro'


#limitar os métodos http permitidos
@app.route('/teste/metodo', methods=['GET'])
def metodo():
    return 'heey'


# retornando o proprio html
@app.route('/html_')
def teste_html():
    return """
    <html>
    <head> 
        <title>Hello</title>
    </head>
    <body>
        <h1>Hello world!</h1>
    </body>
    </html>
    """


if __name__ == '__main__':
    app.run()



# export FLASK_APP = nome.py --> rodar no terminal se o nome não for app.py
# Os nomes das funções não podem ser os mesmos: overwriting
