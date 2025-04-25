from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operador = str(request.form['operador'])
        resultado = 0
        acionar = 0
        if operador == '+':
            resultado = num1+num2
            acionar = 1
        elif operador == '-':
            resultado = num1-num2
            acionar = 1
        elif operador == '*':
            resultado = num1*num2
            acionar = 1
        elif operador == '/':
            if num2 == 0:
                resultado = 'impossível dividir por 0'
                acionar = 1
            else:
                resultado = num1/num2
                acionar = 1
        else:
            resultado = 'operador inexistente'
            acionar = 1
        
        return render_template('index.html',resultado=resultado, acionar=acionar)
    except ValueError as e:
        return render_template('erro.html', mensagem=f"Entrada inválida: {e}")
    finally:
        print("obrigado por usar o programa ")

if __name__ == '__main__':
    app.run(debug=True)