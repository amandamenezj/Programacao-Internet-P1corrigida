from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def pagina_inicial():
    resultado = False # criando a variavel


    if request.method == 'POST':
        nome = request.form['nome']
        peso = request.form['peso']
        altura = request.form['altura']

            # Calculo do formulario
        altura = float(altura)
        peso = float(peso)

        imc = peso / (altura * altura)

        if imc < 18.5:
            mensagem = '🔵 Abaixo do peso'
            cor = 'alert-info'
        elif imc >= 18.5 and imc < 25: # or, um lado certo; and, dois lados certos
            mensagem = '🟢 Peso normal'
            cor = 'alert-success'
        elif imc < 30:
            mensagem = '🟡 Sobrepeso'
            cor = 'alert-warning'
        else:
            mensagem = '🔴 Obesidade'
            cor = 'alert-danger'

        resultado = True 

        return render_template('index.html', nome = nome, peso = peso, altura = altura, mensagem = mensagem, cor = cor, resultado = resultado) # aqui os parametros não funcionam, retorna o index.html, esse RETURN FECHA O IF FILHO

    return render_template('index.html', resultado = resultado) # esse return fecha o IF LÁ DE CIMA

@app.route('/equipe')
def equipe():
    return render_template('equipe.html') # alinhado com equipe


if __name__ == '__main__':
    app.run(debug=True)